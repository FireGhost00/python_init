from tomlkit import value
from os import system
import numeros


def preguntar():
    system('cls')
    print("Bienvenido a la farmacia Python")

    while True:
        print("[P] Perfumeria\n[F] Farmacia\n[C] Cosmetica\n")
        try:
            rubro = input("Ingrese el rubro deseado: ").upper()
            ["P", "F", "C"].index(rubro)
        except ValueError:
            print("Rubro incorrecto")
        else:
            break

    numeros.decorador(rubro)

def iniciar():
    while True:
        preguntar()
        try:
            continuar = input("Desea otro turno? [S] Si [N] No: ").upper()
            ["S", "N"].index(continuar)
        except ValueError:
            print("Opcion incorrecta")
        else:
            if continuar == "N":
                print("Gracias por su visita")
                break
iniciar()