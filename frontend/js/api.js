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
    throw new Error(Array.isArray(det) ? det.map(e => e.msg).join(". ") : det || "Error " + r.status);
  }
  return d;
}

const Api = {
  lotes: () => api("/lotes?solo_activos=true"),
  crearLote: b => api("/lotes", { method: "POST", body: JSON.stringify(b) }),
  parseIA: b => api("/lotes/parse-ia", { method: "POST", body: JSON.stringify(b), timeout: 30000 }),
  reservas: () => api("/reservas"),
  reservar: b => api("/reservas", { method: "POST", body: JSON.stringify(b) }),
  confirmar: (id, n) => api(`/reservas/${id}/confirmar`, { method: "PATCH", body: JSON.stringify({ cantidad_recogida: n }) }),
  cancelar: id => api(`/reservas/${id}/cancelar`, { method: "PATCH" }),
  resumen: ia => api("/resumen?incluir_ia=" + ia),
};
