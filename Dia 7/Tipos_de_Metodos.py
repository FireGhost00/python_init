class Pajaro:

    alas = True
    def __init__(self, nombre, especie, color):
        self.nombre = nombre
        self.especie = especie
        self.color = color

    def piar(self):
        print("Pio, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"El pájaro {self.nombre} voló {metros} metros")

    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")

Pajaro.poner_huevos(3)

piolin = Pajaro("Piolín", "Canario", "Amarillo")

piolin.piar()
piolin.volar(10)


