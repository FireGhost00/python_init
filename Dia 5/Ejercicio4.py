def contar_primos(numero):
    primos = [2]

    iterador = 3

    if numero < 2:
        return 0

    while iterador <= numero:
        for n in range(2, iterador,2):
            if iterador % n == 0:
                iterador += 2
                break
        else:
            primos.append(iterador)
            iterador += 2
    print(primos)
    return len(primos)

print(contar_primos(50))  # 3