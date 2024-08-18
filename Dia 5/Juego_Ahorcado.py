from random import choice

palabras = ['casa', 'perro', 'gato', 'computadora', 'celular', 'teclado', 'raton', 'monitor', 'ventana', 'puerta']

letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


def elegir_palabra(lista):
    palabra_elegida = choice(lista)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    while not es_valida:
        letra_elegida = input('Ingresa una letra: ').lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('Por favor, introduce una letra válida')
    return letra_elegida


def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('_')
    print(' '.join(lista_oculta))


def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in letras_incorrectas or letra_elegida in letras_correctas:
        print('Ya has ingresado esta letra, por favor introduce otra')
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder(palabra_oculta)
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    return vidas, fin, coincidencias


def perder(palabra_oculta):
    print('Perdiste! La palabra era:', palabra_oculta)
    return True


def ganar(palabra_oculta):
    mostrar_nuevo_tablero(palabra_oculta)
    print('Ganaste, has encontrado la palabra!')
    return True


palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas:' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()
    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)
    juego_terminado = terminado
