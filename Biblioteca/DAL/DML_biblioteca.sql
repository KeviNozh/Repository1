INSERT INTO libros (titulo, autor, categoria, editorial) VALUES
('El Principito', 'Antoine de Saint-Exupéry', 'Ficción', 'Editorial XYZ'),
('1984', 'George Orwell', 'Ficción', 'Editorial ABC');

INSERT INTO usuarios (nombre, tipo) VALUES 
('Juan Perez', 'Administrador'),
('Maria Lopez', 'Cliente');

INSERT INTO prestamos (usuario_id, libro_id, fecha_prestamo) VALUES 
(1, 1, '2024-10-01'),
(2, 2, '2024-10-03');