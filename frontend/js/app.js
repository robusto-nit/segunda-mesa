const $ = s => document.querySelector(s);
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const lista = x => Array.isArray(x) ? x : (x?.lotes ?? x?.reservas ?? x?.items ?? []);
const tit = k => { k = k.replace(/_/g, " "); return k[0].toUpperCase() + k.slice(1); };

let tAviso;
function aviso(msg, error) {
  const t = $("#aviso");
  t.textContent = msg; t.className = error ? "error" : "ok"; t.hidden = false;
  clearTimeout(tAviso); tAviso = setTimeout(() => t.hidden = true, 6000);
}
async function accion(fn, ok, despues) {
  try { await fn(); aviso(ok); despues && despues(); } catch (e) { aviso(e.message, true); }
}
function restante(h) {
  const m = Math.round((new Date(h) - Date.now()) / 6e4);
  if (isNaN(m)) return ["", false];
  if (m <= 0) return ["Vencido", true];
  return [m < 60 ? `Quedan ${m} min` : `Quedan ${Math.floor(m / 60)} h ${m % 60} min`, m < 60];
}

/* Disponibles */
async function cargarLotes() {
  const el = $("#lista-lotes");
  el.innerHTML = '<p class="vacio">Cargando…</p>';
  try {
    const ls = lista(await Api.lotes());
    el.innerHTML = ls.length ? ls.map(l => {
      const disp = l.cantidad_disponible ?? l.disponible ?? l.cantidad_total;
      const [txt, urg] = restante(l.hora_limite);
      return `<article class="lote" data-id="${esc(l.id)}">
        <div class="tiempo ${urg ? "urgente" : ""}">${esc(txt)}</div>
        <h3>${esc(l.alimento)}</h3>
        <p>${esc(disp)} ${esc(l.unidad)} disponibles de ${esc(l.cantidad_total)}</p>
        <p>${esc(l.lugar)} · Responsable: ${esc(l.responsable)}</p>
        ${l.consejo_conservacion ? `<p>${esc(l.consejo_conservacion)}</p>` : ""}
        <div class="fila"><input type="number" min="1" max="${esc(disp)}" value="1" aria-label="Cantidad a reservar">
        <button data-reservar>Reservar</button></div></article>`;
    }).join("") : '<p class="vacio">No hay excedentes publicados. Publica el primero desde la pestaña Publicar.</p>';
  } catch (e) { el.innerHTML = ""; aviso(e.message, true); }
}
$("#lista-lotes").addEventListener("click", e => {
  const b = e.target.closest("[data-reservar]"); if (!b) return;
  const c = b.closest(".lote"), nombre = $("#nombre").value.trim();
  if (nombre.length < 2) return aviso("Escribe tu nombre arriba para poder reservar", true);
  localStorage.setItem("nombre", nombre);
  accion(() => Api.reservar({ lote_id: +c.dataset.id, receptor_nombre: nombre, cantidad_reservada: +c.querySelector("input").value }),
    "Reserva creada", cargarLotes);
});

/* Publicar */
$("#form-lote").addEventListener("submit", e => {
  e.preventDefault();
  const f = Object.fromEntries(new FormData(e.target));
  f.cantidad_total = +f.cantidad_total;
  f.hora_limite += ":00";
  if (!f.consejo_conservacion) delete f.consejo_conservacion;
  if (!f.categoria) delete f.categoria;
  accion(() => Api.crearLote(f), "Excedente publicado", () => { e.target.reset(); location.hash = "disponibles"; });
});
$("#btn-ia").addEventListener("click", async () => {
  const f = $("#form-lote"), b = $("#btn-ia");
  if ($("#nota").value.trim().length < 4) return aviso("Escribe primero una nota de al menos 4 caracteres", true);
  b.disabled = true; b.textContent = "Interpretando…";
  try {
    const r = await Api.parseIA({ texto_libre: $("#nota").value.trim(), responsable: f.responsable.value || undefined, lugar: f.lugar.value || undefined, publicar_automaticamente: false });
    const lotes = r.vista_previa ?? [];
    if (!lotes.length) throw new Error("La IA no detectó ningún alimento en la nota.");
    const d = { ...lotes[0], cantidad_total: lotes[0].cantidad };
    for (const [k, v] of Object.entries(d)) {
      const i = f.elements[k];
      if (i && v != null) i.value = k === "hora_limite" ? String(v).slice(0, 16) : v;
    }
    const l0 = lotes[0];
    // El backend devuelve un borrador de respaldo cuando Gemini no responde
    const respaldo = l0.respaldo || (l0.unidad === "lote" && l0.cantidad === 1 && /^Mantener en lugar fresco/.test(l0.consejo_conservacion || ""));
    if (respaldo) aviso("La IA no respondió y se cargó un borrador sin interpretar. Completa los campos a mano o intenta de nuevo en unos minutos.", true);
    else aviso(lotes.length > 1
      ? `La IA detectó ${lotes.length} alimentos. Cargué el primero: publícalo y repite con el siguiente.`
      : "Revisa lo que propuso la IA y publica cuando esté correcto");
  } catch (e) { aviso(e.message, true); }
  finally { b.disabled = false; b.textContent = "Completar con IA"; }
});

/* Reservas */
async function cargarReservas() {
  const el = $("#lista-reservas");
  el.innerHTML = '<p class="vacio">Cargando…</p>';
  try {
    const rs = lista(await Api.reservas());
    el.innerHTML = rs.length ? rs.map(r => {
      const abierta = !/cancel|recog|confirm/i.test(r.estado || "");
      return `<article class="lote" data-id="${esc(r.id)}">
        <h3>Lote ${esc(r.lote_id)}: ${esc(r.cantidad_reservada)} reservadas</h3>
        <p>${esc(r.receptor_nombre)}</p>
        <p class="estado">${esc(r.estado || "")}${r.cantidad_recogida != null ? ` · Recogido: ${esc(r.cantidad_recogida)}` : ""}</p>
        ${abierta ? `<div class="fila"><input type="number" min="0" value="${esc(r.cantidad_reservada)}" aria-label="Cantidad recogida">
        <button data-confirmar>Confirmar recogida</button><button class="peligro" data-cancelar>Cancelar</button></div>` : ""}</article>`;
    }).join("") : '<p class="vacio">Aún no hay reservas.</p>';
  } catch (e) { el.innerHTML = ""; aviso(e.message, true); }
}
$("#lista-reservas").addEventListener("click", e => {
  const c = e.target.closest(".lote"), id = c && c.dataset.id;
  if (e.target.closest("[data-confirmar]"))
    accion(() => Api.confirmar(id, +c.querySelector("input").value), "Recogida confirmada", cargarReservas);
  if (e.target.closest("[data-cancelar]"))
    accion(() => Api.cancelar(id), "Reserva cancelada", cargarReservas);
});

/* Resumen: primero los números, luego la IA aparte */
const ETIQ = {
  total_publicado: "Publicado",
  reservado_pendiente: "Reservado, sin recoger",
  efectivamente_recogido: "Recogido",
  expirado_sin_rescate: "Expirado sin rescate",
  tasa_rescate_porcentaje: "Tasa de rescate (%)",
};
const metricas = m => Object.entries(m || {})
  .map(([k, v]) => `<div class="dato"><b>${esc(v)}</b><span>${esc(ETIQ[k] || tit(k))}</span></div>`).join("");

async function cargarResumen() {
  const el = $("#resumen-datos"), ia = $("#resumen-ia");
  ia.innerHTML = ""; el.innerHTML = '<p class="vacio">Cargando…</p>';
  try { el.innerHTML = metricas((await Api.resumen(false)).metricas); }
  catch (e) { el.innerHTML = ""; return aviso(e.message, true); }
  ia.innerHTML = '<p class="vacio" role="status"><span class="giro"></span>La IA está redactando observaciones…</p>';
  try {
    const recs = (await Api.resumen(true)).recomendaciones_ia;
    ia.innerHTML = recs && recs.length
      ? `<h2>Observaciones</h2><div class="bloque"><ul>${recs.map(x => `<li>${esc(x)}</li>`).join("")}</ul></div>`
      : '<p class="vacio">Aún no hay datos suficientes para generar observaciones.</p>';
  } catch { ia.innerHTML = '<p class="vacio">No se pudieron generar las observaciones. Los números de arriba siguen vigentes.</p>'; }
}

/* Navegación por pestañas */
const vistas = { disponibles: cargarLotes, publicar: () => {}, reservas: cargarReservas, resumen: cargarResumen };
function ruta() {
  const v = vistas[location.hash.slice(1)] ? location.hash.slice(1) : "disponibles";
  document.querySelectorAll("main > section").forEach(s => s.hidden = s.id !== v);
  document.querySelectorAll("nav a").forEach(a => a.setAttribute("aria-current", a.hash === "#" + v ? "page" : "false"));
  vistas[v]();
}
$("#nombre").value = localStorage.getItem("nombre") || "";
addEventListener("hashchange", ruta);
ruta();
