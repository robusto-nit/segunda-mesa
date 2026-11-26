import sqlite3

DB_PATH = "segunda_mesa.db"

def get_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS lotes_excedentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alimento TEXT NOT NULL,
            categoria TEXT DEFAULT 'General',
            cantidad_total INTEGER NOT NULL,
            cantidad_disponible INTEGER NOT NULL,
            unidad TEXT NOT NULL,
            lugar TEXT DEFAULT 'Cafetería Principal',
            responsable TEXT NOT NULL,
            hora_limite TEXT NOT NULL,
            urgencia TEXT DEFAULT 'Media',
            consejo_conservacion TEXT DEFAULT '',
            estado TEXT DEFAULT 'activo',
            creado_en TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lote_id INTEGER NOT NULL,
            receptor_nombre TEXT NOT NULL,
            cantidad_reservada INTEGER NOT NULL,
            cantidad_recogida INTEGER DEFAULT 0,
            estado TEXT DEFAULT 'reservado',
            creado_en TEXT NOT NULL,
            FOREIGN KEY (lote_id) REFERENCES lotes_excedentes(id)
        );
    """)
    conn.commit()
    conn.close()