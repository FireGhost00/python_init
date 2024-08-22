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

piolin = Pajaro("Piolín", "Canario", "Amarillo")

piolin.piar()
piolin.volar(10)


