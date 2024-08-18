'''
this program is a simple calculator that performs the operations of addition,
 subtraction, multiplication and division.
'''


print("------------------------------------")
print("        Calculadora simple          ")
print("------------------------------------")
name = input("Hola! Cual es tu nombre? ")

print(f"Bienvenido {name},las operaciones validas son las siguientes")
print("1 - Sumar")
print("2 - Restar")
print("3 - Multiplicar")
print("4 - Dividir")
print("5 - Salir")

val1 = 0
val2 = 0
opc =  0
name = ""

def calculadora(x, y, z):
    """
    Performs the arithmetic operation specified by z on the operands x and y.

    Args:
        x (int): The first operand.
        y (int): The second operand.
        z (int): The operation to perform (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division).

    Returns:
        str: The result of the arithmetic operation, or an error message if the operation is invalid.
    """
    if z == 1:
        return f'El resultado de la suma es: {x + y}'
    elif z == 2:
        return f'El resultado de la resta es: {x - y}'
    elif z == 3:
        return f'El resultado de la multiplicación es: {x * y}'
    elif z == 4:
        if y == 0:
            return "No se puede dividir por 0"
        return f'El resultado de la división es: {x / y}'
    else:
        return "Por favor, introduce una opción válida"

while opc != 5:


    try:
        opc = int(input("Que operación deseas realizar? "))
        if opc not in range(1, 6):
            print("Por favor, introduce una opción válida")
            continue
        if opc == 5:
            print("Gracias por usar la calculadora")
            break
        val1 = int(input("Introduce el primer número: "))
        val2 = int(input("Introduce el segundo número: "))
    except ValueError:
        print("Por favor, introduce un número")
        continue
    if val1 == 0 or val2 == 0 and opc != 5:
        print("Por favor, introduce un número diferente de 0")
        continue
    if val1 != 0 or val2 != 0 and opc == 5:
        calculadora(val1, val2, opc)
        print(calculadora(val1, val2, opc))






'''
respuesta = multiplicar(3, 5)

print(f'La respuesta de la multiplicacion es {respuesta}')
'''