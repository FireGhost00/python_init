def decorar_saludo(funcion):

    def nueva_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')
    return nueva_funcion


def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())

mayusculas('Python')

minusculas('Python')

mayusculas_decorado = decorar_saludo(mayusculas)

mayusculas_decorado('Nelson')