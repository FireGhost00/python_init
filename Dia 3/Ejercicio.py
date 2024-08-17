texto = input("Ingrese un texto: ").lower()
letras = input("Ingrese tres letras: ").lower()


lista = list(letras)

texto_al_revez = ''.join(reversed(texto))

total_letra1 = texto.count(lista[0])

total_letra2 = texto.count(lista[1])

total_letra3 = texto.count(lista[2])

total_palabras = len(list(texto.split()))

print("\n")

print(f"El total de '{lista[0]}' dentro del texto es {total_letra1} ")
print(f"El total de '{lista[1]}' dentro del texto es {total_letra2} ")
print(f"El total de '{lista[2]}' dentro del texto es {total_letra3} ")


print("----------------------")

print(f"En el texto hay un total de {total_palabras} palabras")

print("----------------------")
print(f"La primera letra del texto es  {texto[0]} y la ultima es {texto[-1]}")
print("----------------------")
print(texto_al_revez)
print("----------------------")

if "Python" in texto:
    print("La palabra Python se encuentra dentro del texto")
else:
    print("La palabra Python no se encuentra dentro del texto")






