'''
monedas = 5

while monedas > 0:
    print("Tienes", monedas, "monedas")
    monedas = monedas - 1
else:
    print("Te has quedado sin monedas")
    '''

respuesta = 'S'

while respuesta == 'S':
    respuesta = input("Quieres que te salude de nuevo? (S/N): ").upper()
    if respuesta != 'S':
        print("Adios!")
        break
    print("Hola!")
#else:
 #   print("Adios!")
