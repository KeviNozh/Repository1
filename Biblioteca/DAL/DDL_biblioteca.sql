CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor TEXT,
    categoria TEXT,
    editorial TEXT
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    tipo TEXT
);

CREATE TABLE IF NOT EXISTS prestamos (
    id INTEGER PRIMARY KEY,
    usuario_id INTEGER,
    libro_id INTEGER,
    fecha_prestamo TEXT,
    fecha_devolucion TEXT
);