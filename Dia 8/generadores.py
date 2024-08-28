def mi_funcion():
    lista = []
    for i in range(1, 5):
        lista.append(i*10)
    return lista

def mi_generador():
    for i in range(1, 5):
        yield i*10

print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))
print(next(g))


def multiplos_siete():
    num = 1
    while True:
        yield 7 * num
        num += 1


generador = multiplos_siete()



def mensaje():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x


perder_vida = mensaje()
