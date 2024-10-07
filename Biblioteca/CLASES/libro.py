class Libro:
    def __init__(self, id, titulo, autor, categoria, editorial):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.editorial = editorial

    def __str__(self):
        return f'{self.titulo} por {self.autor}'
    