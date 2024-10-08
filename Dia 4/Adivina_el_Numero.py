from random import randint

intentos = 0
intento = 0

numero_secreto = randint(1, 100)

nombre = input("Hola! Cual es tu nombre? ")

print(f"Bienvenido {nombre}! Estoy pensando en un numero entre 1 y 100\n Tienes 8 intentos para adivinar!")

while intentos < 8:
    try:
        intento = int(input("Cual es tu número? "))
        if intento not in range(1, 101):
            print("Por favor, introduce un numero entre 1 y 100")
            continue
    except ValueError:
        print("Por favor, introduce un numero")
        continue
    intentos += 1
    if intento < numero_secreto:
        print("Muy bajo! te quedan ", 8 - intentos, " intentos")
    elif intento > numero_secreto:
        print("Muy alto! te quedan ", 8 - intentos, " intentos")
    else:
        print(f"Felicidades {nombre}! Adivinaste el numero en {intentos} intentos!")
        break

if intento != numero_secreto:
    print(f"Lo siento {nombre}, el  numero era {numero_secreto}")