from clases.libro import Libro
from clases.usuario import Usuario
from clases.prestamo import Prestamo
from auxiliares.utils import calcular_multa

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        if isinstance(libro, Libro):
            self.libros.append(libro)

    def agregar_usuario(self, usuario):
        if isinstance(usuario, Usuario):
            self.usuarios.append(usuario)

    def prestar_libro(self, libro_id, usuario_id, fecha_prestamo):
        libro = self.buscar_libro(libro_id)
        usuario = self.buscar_usuario(usuario_id)
        prestamo = Prestamo(usuario, libro, fecha_prestamo)
        self.prestamos.append(prestamo)
        return prestamo

    def calcular_multa(self, prestamo, fecha_devolucion):
        return calcular_multa(prestamo.fecha_prestamo, fecha_devolucion)

    def buscar_libro(self, libro_id):
        return next((libro for libro in self.libros if libro.id == libro_id), None)

    def buscar_usuario(self, usuario_id):
        return next((usuario for usuario in self.usuarios if usuario.id == usuario_id), None)
