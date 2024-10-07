class DetalleLibro:
    def __init__(self, libro, fecha_prestamo, fecha_devolucion=None):
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def devolver_libro(self, fecha_devolucion):
        self.fecha_devolucion = fecha_devolucion
