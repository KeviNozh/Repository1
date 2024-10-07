class Editorial:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def publicar_libro(self, titulo):
        return f'La editorial {self.nombre} ha publicado el libro titulado {titulo}.'
