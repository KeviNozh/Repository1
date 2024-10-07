from clases.paises import pais_existe

class Autor:
    def __init__(self, id, nombre, pais):
        if not pais_existe(pais):
            raise ValueError("El país no es válido.")
        self.id = id
        self.nombre = nombre
        self.pais = pais

    def escribir_libro(self, titulo):
        return f'{self.nombre} ha escrito el libro titulado {titulo}.'

    def __str__(self):
        return f'Autor: {self.nombre} de {self.pais}.'
