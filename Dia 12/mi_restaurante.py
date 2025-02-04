from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

# Crear la ventana principal
aplicacion = Tk()


# tama;o de la ventana
aplicacion.geometry('1020x630+0+0')

# evitar maximizar
aplicacion.resizable(0,0)

# Titulo de la ventana
aplicacion.title('Mi Restaurante - Sistema de Facturacion')

# Color de fondo de la ventanda
aplicacion.config(bg='burlywood')

panel_superior = Frame(aplicacion, bd=1, relief="flat")
panel_superior.pack(side=TOP)

etiqueta_titulo = Label(panel_superior, text='Sistema de facturacion',fg='azure4',
                        font=('Dosis', 58), bg='burlywood', width=20)

etiqueta_titulo.grid(row=0, column=0)

#panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief="flat")
panel_izquierdo.pack(side=LEFT)

#panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief="flat")
panel_costos.pack(side=BOTTOM)
#panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comidas', font=('Dosis', 19,'bold'), bd=1,fg='azure4', relief="flat")
panel_comidas.pack(side=LEFT)
#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19,'bold'), bd=1,fg='azure4', relief="flat")
panel_bebidas.pack(side=LEFT)

#panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19,'bold'), bd=1,fg='azure4', relief="flat")
panel_postres.pack(side=LEFT)
#panel derecho
panel_derecha = Frame(aplicacion, bd=1, relief="flat")
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief="flat", background='burlywood')
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief="flat", background='burlywood')
panel_recibo.pack()

#panel botones
panel_botones = Frame(panel_derecha, bd=1, relief="flat", background='burlywood')
panel_botones.pack()





#Evitar que la pantalla se cierre
aplicacion.mainloop()

