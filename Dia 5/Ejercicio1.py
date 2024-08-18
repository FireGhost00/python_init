def devolver_distintos(a,b,c):
    """
    Returns the number of different arguments.

    Args:
        a (int): The first number.
        b (int): The second number.
        c (int): The third number.

    Returns:
        int: The number of different arguments.


    """
    suma = a + b + c
    lista = [a,b,c]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]

print(devolver_distintos(5,4,3))