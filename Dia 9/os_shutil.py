import os
import shutil
archivo = open('curso.txt','w')
archivo.write('Curso de Python')
archivo.close()

shutil.move('curso.txt','Dia 9/curso.txt')
