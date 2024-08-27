class Cd:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"Album: {self.titulo}\nAutor: {self.autor}\nCanciones: {', '.join(self.canciones)}"

mi_cd = Cd("Queen", "Greatest Hits", ["Bohemian Rhapsody", "Another One Bites the Dust", "We Will Rock You"])

#print(f"El CD {mi_cd.titulo} de {mi_cd.autor} contiene las siguientes canciones:")

print(mi_cd)