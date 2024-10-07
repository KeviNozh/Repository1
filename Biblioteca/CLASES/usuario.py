class Usuario:
    def __init__(self, id, nombre, tipo_usuario):
        self.id = id
        self.nombre = nombre
        self.tipo_usuario = tipo_usuario

    def __str__(self):
        return self.nombre
    