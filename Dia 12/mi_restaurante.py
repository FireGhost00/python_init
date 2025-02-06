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
panel_costos = Frame(panel_izquierdo, bd=1, relief="flat",bg='azure4',padx=50)
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

#Lista de productos
lista_comidas = ['pollo', 'carne', 'pescado', 'pasta', 'pizza', 'hamburguesa', 'tacos', 'sushi', 'ensalada', 'sopa']
lista_bebidas = ['agua', 'refresco', 'cafe', 'te', 'jugo', 'cerveza', 'vino', 'whisky', 'ron', 'vodka']
lista_postres = ['pastel', 'helado', 'gelatina', 'pay', 'churros', 'galletas', 'brownies', 'flan', 'crepas', 'chocolate']

#Generar items de la lista de comidas
variables_comidas = []
cuadros_comidas = []
texto_comidas = []
contador = 0
for comida in lista_comidas:

    # crear checkbutton
    variables_comidas.append('')
    variables_comidas[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comidas[contador])
    comida.grid(row=contador,
                column=0,
                sticky=W)
    # crear los cuadros de entradas
    cuadros_comidas.append('')
    texto_comidas.append('')
    texto_comidas[contador] = StringVar()
    texto_comidas[contador].set('0')
    cuadros_comidas[contador] = Entry(panel_comidas,
                                      font=('Dosis', 18,'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_comidas[contador])
    cuadros_comidas[contador].grid(row=contador,
                                      column=1,
                                      sticky=W)
    contador += 1

#Generar items de la lista de comidas
variables_bebidas = []
cuadros_bebidas = []
texto_bebidas= []
contador = 0
for bebida in lista_bebidas:
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebidas[contador])
    bebida.grid(row=contador,
                column=0,
                sticky=W)
    # crear los cuadros de entradas
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bebidas,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador,
                                   column=1,
                                   sticky=W)
    contador += 1

#Generar items de la lista de postres
variables_postres = []
cuadros_postres = []
texto_postres= []
contador = 0
for postre in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 19,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postres[contador])
    postre.grid(row=contador,
                column=0,
                sticky=W)
    # crear los cuadros de entradas
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                   column=1,
                                   sticky=W)
    contador += 1


#varaibales
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# etiquetas de costo y campo de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12,'bold'),
                              fg='white',
                              bg='azure4')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                            font=('Dosis', 12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_comida)

texto_costo_comida.grid(row=0, column=1,padx=41)



# etiquetas de costo y campo de entrada
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12,'bold'),
                              fg='white',
                              bg='azure4')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                            font=('Dosis', 12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1, column=1,padx=41)



# etiquetas de costo y campo de entrada
etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postre',
                              font=('Dosis', 12,'bold'),
                              fg='white',
                              bg='azure4')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                            font=('Dosis', 12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_postre)

texto_costo_postre.grid(row=2, column=1,padx=41)

# etiquetas de costo y campo de entrada
etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Dosis', 12,'bold'),
                              fg='white',
                              bg='azure4')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                            font=('Dosis', 12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_subtotal)

texto_subtotal.grid(row=0, column=3,padx=41)

etiqueta_impuesto = Label(panel_costos,
                              text='Impuestos',
                              font=('Dosis', 12,'bold'),
                              fg='white',
                              bg='azure4')
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos,
                            font=('Dosis', 12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_impuesto)

texto_impuesto.grid(row=1, column=3,padx=41)


etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12,'bold'),
                              fg='white',
                              bg='azure4')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                            font=('Dosis', 12,'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_total)

texto_total.grid(row=2, column=3,padx=41)



#Evitar que la pantalla se cierre
aplicacion.mainloop()

