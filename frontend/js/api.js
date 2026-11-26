// Todas las llamadas al backend viven aquí. Cambia API_URL si el backend corre en otro lado.
const API_URL = "http://127.0.0.1:8000";

async function api(ruta, opciones = {}) {
  const { timeout = 60000, ...resto } = opciones;
  const ctl = new AbortController();
  const t = setTimeout(() => ctl.abort(), timeout);
  let r;
  try {
    r = await fetch(API_URL + ruta, { headers: { "Content-Type": "application/json" }, signal: ctl.signal, ...resto });
  } catch (e) {
    throw new Error(e.name === "AbortError"
      ? "El servidor tardó demasiado en responder. Intenta de nuevo o llena el formulario a mano."
      : "No se pudo conectar con el servidor. Revisa que el backend esté encendido.");
  } finally { clearTimeout(t); }
  const d = await r.json().catch(() => null);
  if (!r.ok) {
    const det = d && d.detail;
    throw new Error(Array.isArray(det) ? det.map(traducir).join(". ") : det || "Error " + r.status);
  }
  return d;
}

const TRAD = [
  [/greater than or equal to 0/i, "no puede ser negativo"],
  [/greater than 0/i, "debe ser mayor que 0"],
  [/at least (\d+) character/i, "escribe al menos $1 caracteres"],
  [/valid integer/i, "debe ser un número entero"],
  [/valid datetime/i, "fecha u hora no válida"],
  [/field required/i, "es obligatorio"],
];
function traducir(e) {
  const campo = String(e.loc?.at(-1) ?? "").replace(/_/g, " ");
  let m = e.msg;
  for (const [re, t] of TRAD) { const x = re.exec(e.msg); if (x) { m = t.replace("$1", x[1]); break; } }
  return (campo ? campo[0].toUpperCase() + campo.slice(1) + ": " : "") + m;
}

const Api = {
  lotes: () => api("/lotes?solo_activos=true"),
  todosLotes: () => api("/lotes?solo_activos=false"),
  crearLote: b => api("/lotes", { method: "POST", body: JSON.stringify(b) }),
  parseIA: b => api("/lotes/parse-ia", { method: "POST", body: JSON.stringify(b), timeout: 40000 }),
  reservas: () => api("/reservas"),
  reservar: b => api("/reservas", { method: "POST", body: JSON.stringify(b) }),
  confirmar: (id, n) => api(`/reservas/${id}/confirmar`, { method: "PATCH", body: JSON.stringify({ cantidad_recogida: n }) }),
  cancelar: id => api(`/reservas/${id}/cancelar`, { method: "PATCH" }),
  resumen: ia => api("/resumen?incluir_ia=" + ia),
};
