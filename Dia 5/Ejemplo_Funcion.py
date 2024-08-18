precios_cafe = [('capuchino', 2.5), ('latte', 3.0), ('mocha', 3.5)]


def cafe_mas_caro(precios_cafe):
    """
    Returns the most expensive coffee in the list.

    Args:
        precios_cafe (list): A list of tuples containing the name and price of different types of coffee.

    Returns:
        tuple: The name and price of the most expensive coffee in the list.
    """
    mas_caro = precios_cafe[0]
    precio_mayor = 0
    for cafe,precio in precios_cafe:
        if precio > precio_mayor:
            precio_mayor = precio
            mas_caro = cafe
        else:
            pass
    return (mas_caro, precio_mayor)


print(f'EL cafe mas caro es {cafe_mas_caro(precios_cafe)[0]} y cuesta {cafe_mas_caro(precios_cafe)[1]} dolares')

for elemento in precios_cafe:
    print(f'El precio del {elemento[0]} es de {elemento[1]} dolares')