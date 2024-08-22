from queue import PriorityQueue


class Pajaro:

    def __init__(self, nombre, especie, color):
        self.nombre = nombre
        self.especie = especie
        self.color = color


mi_pajaro = Pajaro("Piolín", "Canario", "Amarillo")

print(f'Mi pájaro se llama {mi_pajaro.nombre}, es de la especie {mi_pajaro.especie} y es de color {mi_pajaro.color}')

'''

list = [mi_pajaro.nombre, mi_pajaro.especie, mi_pajaro.color]
for i in list:
    print(i.upper())
    '''