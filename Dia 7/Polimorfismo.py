from typing import overload


class Vaca:
    def __init__(self,nomre):
        self.nombre = nomre

    def hablar(self):
        print(self.nombre +' Muuuu')

class Oveja:
    def __init__(self,nomre):
        self.nombre = nomre

    def hablar(self):
        print(self.nombre +' Beeee')

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Dolly')

vaca1.hablar()
oveja1.hablar()


animales = [vaca1,oveja1]

for animal in animales:
    animal.hablar()


def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)