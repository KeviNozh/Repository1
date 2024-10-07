from datetime import datetime

class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None

    def devolver(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion