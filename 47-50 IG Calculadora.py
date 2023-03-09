'''
	* TEMA 47

	---- CREACIÓN DE UNA INTERFAZ GRÁFICA ----

					CALCULADORA
'''
'''
	* TEMA 48

	---- FUNCIONALIDAD DE LA CALCULADORA----

-> Sa va a conseguir que cuando pulsemos los botones aparezcan en pantalla.
-> Para ello debemos hacer una llamada a una funcion desde cada boton.
 
'''
'''
	* TEMA 49

	---- FUNCIONALIDAD DE LA CALCULADORA----

-> Comenzamos a dar funcionalidad a las operaciones, empezando por suma.
 
'''


from tkinter import *

raiz = Tk()

miFrame = Frame(raiz)

miFrame.pack()

operacion = ""

resultado = 0

#----------Pantalla----------------------------------------
# Se ha usado "columnspan" para hacer que la fila ocupe 4 columnas en la pantalla numérica.

numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg='black', fg='#03f943', justify='right')

#----------Pulsaciones teclado----------------------------

def numeroPulsado(num):
	global operacion

	if operacion != "":
		
		numeroPantalla.set(num)

		operacion = ""

	else:
		numeroPantalla.set(numeroPantalla.get() + num)

#----------Funcion Suma------------------------------------

def suma(num):
	global operacion

	global resultado

	resultado += float(num)

	operacion = "suma"

	numeroPantalla.set(resultado)

#-----------Funcion el_resultado---------------------------

def el_resultado():
	
	global resultado

	numeroPantalla.set(resultado + float(numeroPantalla.get()))

	resultado = 0

#------------Funcion Resta--------------------------------

def resta(num):
	global operacion
	
	global resultado

	resultado -= float(num)

	operacion = "resta"

	numeroPantalla.set(resultado)

#----------Fila 1------------------------------------------

boton7 = Button(miFrame, text='7', width=3, command=lambda:numeroPulsado('7'))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text='8', width=3, command=lambda:numeroPulsado('8'))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text='9', width=3, command=lambda:numeroPulsado('9'))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame, text='/', width=3)
botonDiv.grid(row=2, column=4)

#----------Fila 2------------------------------------------

boton4 = Button(miFrame, text='4', width=3, command=lambda:numeroPulsado('4'))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text='5', width=3, command=lambda:numeroPulsado('5'))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text='6', width=3, command=lambda:numeroPulsado('6'))
boton6.grid(row=3, column=3)
botonPor = Button(miFrame, text='X', width=3)
botonPor.grid(row=3, column=4)


#----------Fila 3------------------------------------------

boton1 = Button(miFrame, text='1', width=3, command=lambda:numeroPulsado('1'))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text='2', width=3, command=lambda:numeroPulsado('2'))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text='3', width=3, command=lambda:numeroPulsado('3'))
boton3.grid(row=4, column=3)
botonRes = Button(miFrame, text='-', width=3, command=lambda:resta(numeroPantalla.get()))
botonRes.grid(row=4, column=4)


#----------Fila 4------------------------------------------

boton0 = Button(miFrame, text='0', width=3, command=lambda:numeroPulsado('0'))
boton0.grid(row=5, column=1)
botonComa = Button(miFrame, text='.', width=3, command=lambda:numeroPulsado('.'))
botonComa.grid(row=5, column=2)
botonIgual = Button(miFrame, text='=', width=3, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSum = Button(miFrame, text='+', width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4) 











raiz.mainloop()