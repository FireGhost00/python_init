archivo = open('prueba.txt', 'w')

archivo.write('Hola, mundo!')
archivo.close()
archivo = open('prueba.txt')
print(archivo.read())

archivo.close()