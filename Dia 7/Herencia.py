class Animal:

    def __init__(self, edad,color):
        self.edad = edad
        self.color = color


    def nacer(self):
        print("Este animal ha nacido")


class Pajaro(Animal):

    def __init__(self,edad,color,altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo


    def hablas(self):
        print('Pio')

    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')


pio = Pajaro(2,"Amarillo",60)

mi_animal = Animal(5,'negro')
pio.nacer()
print(pio.edad)
