def letras_Unicas(palabra):

    mi_set = set()

    for letra in palabra:
        mi_set.add(letra)

    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista

print(letras_Unicas('entretenido'))  # ['d', 'e', 'i', 'n', 'o', 'r', 't']