'''

	* TEMA 42

	---- INTERFACES GRAFICAS 1/13----

	-> Creación de interfaces gráficas.

		> Librería "Tkinter".
		 También denominadas "GUI", son intermediarios entre el programa
		 y el usuario. Formadas por un conjunto de gráficos como ventanas,
		 botones, menús, casillas de verificación etc.

		> Librerías con las que trabajar para crear GUI.
		 - Tkinter
		 - WxPython
		 - PyQT
		 - PyGTK

		> Tkinter es un "puente" entre Python y la librería TCL/TK


	-> Estructura de ventana con Tkinter

		> 1º Construir una ventana Raíz.
		> 2º De forma habitual se suele crear un Frame dentro de la ventana
			Raiz como aglutinador de elementos(widgets: botones, desplegables, etc...).
'''


	# Construcción de la Raiz.

from tkinter import *

raiz = Tk() # Ventana raiz.

	# Modificación de los atributos de la ventana raiz que trae por defecto.

raiz.title("Guardia Ludica") # Cambiar el nombre de la ventana.

# Le damos dos parametros ancho(width) y alto(height). 0,0 es gigual que Fase, False
# Si cambiamos un 0 por un 1 indicamos si podemos modificar el alto o el ancho.
raiz.resizable(0, True) # Para impedir que la ventana se expanda con el raton.

# Para cambiar el icono de la esquina izquierda.
raiz.iconbitmap("Dado.ico")

# Redimensión de la ventana raiz que viene por defecto.
raiz.geometry("650x400")

# Metodo "config" con el que a parte de otras cosas podemos cambiar el color de fondo.
raiz.config(bg="blue")

raiz.mainloop() # Bucle infinito para que la ventana quede en ejecución, es decir, a la espera de instrucciones.

'''
-------> Para hacer que la ventana no necesitemos de la consola para abrirla o no se nos abra por defecto por
		detras, el archivo ".py" le cambiamos la extensión por ".pyw". De esta forma podemos abrirla desde Window.
'''

'''
	* TEMA 43
	
	---- CREANDO EL "FRAME" 2/13----

	Para crearlo debemos hacer dos cosas:

	-> 1º Crear la linea "miframe = Frame()" para crear el frame.
	-> 2º Empaquetarlo introduciendolo en la raiz 
'''

from tkinter import *

raiz = Tk() 

raiz.title("Guardia Ludica") 

raiz.iconbitmap("Dado.ico")

raiz.config(bg="blue")

miFrame = Frame() # Creación del Frame

miFrame.pack(side="left", anchor="n") # Empaquetando el frame dentro de la raiz. Si damos opciones dentro de "pack"
										# podemos carbiar las opciones del frame.

miFrame.Frame(bg="red") # Dando color al frame

miFrame.config(width="650", height="300") # Tamaño del frame, no se verá hasta darle tamaño.

miFrame.config(bd=20) # Añadiendole un borde al frame



miFrame.config(relief="groove")

raiz.mainloop()


'''
	* TEMA 44

	---- COMO TRABAJAR CON LOS Widget Label 3/13----

	-> Wigets utilizados para mostrar texto o imagenes.
	-> Tienen como única finalidad mostrar texto, no se puede interactura
		con él (borrar, arrastrar, etc...)

	SINTAXIS:  variableLabel = Label(contenedor, opciones)

	OPCIONES: text, ancho, color, fuente, alineación, etc..

'''

from tkinter import *

root = Tk()

miFrame = Frame(root, width=400, height=300)

miFrame.pack()

miImagen = PhotoImage(file="LogoGL.png") # colocando una imangen

Label(miFrame, image=miImagen).place(x=100,y=100)

miLabel = Label(miFrame, text='Hola Mundo', fg="red", font=("Comic Sans MS", 18))

miLabel.place(x=100, y=200) #Place, para colocar el texto en un lugar determinado.

# Label(miFrame, text='Hola Mundo', fg="red").place(x=100, y=200)-> Metodo abrebiado del las dos lineas
# anteriores.

root.mainloop()

'''
	* TEMA 45
	
	---- COMO TRABAJAR CON LOS Widget Entry 4/13----

	-> Wigets(ventana) utilizados para introducir texto.
		Se utilizan de forma similar a como he han usado los Label.

	-> Tienen como única finalidad mostrar texto, no se puede interactuar con él (borrar, arrastra, etc)

'''

from tinker import *

root = tk()

miFrame = Frame(root, width=600, height=400)
miFrame.pack()

cuadroNombre = Entry(miFrame)	# Crea el cuadro de texto
cuadroNombre.grid(row=0, column=0) # Ubica el cuadro en una regilla, fila=0, columna=0

nombreLabel = label(miFrame, text='Nombre: ') # Crea un texto con "Nombre:"
''' Coloca el texto en la fila=0, columna=0, antes del cuadro de Texto.
"sticky" nos permite colocar texto con alineación, con la letra de los puntos cardinales.
Y el "pady" o el "padx", damos un margen a los objetos.'''
nombreLabel.grid(row=0, column=1, sticky="e", pady=30)
nombreLabel.config(fg="red") # Con "config" estamos cambiando los parametros del texto, rojo en este caso.
nombreLabel.config(show="*") # Nos cambia las letras por * como cuando lo utilizaremos para un password

root.mainloop()

'''
	* TEMA 46

	---- COMO TRABAJAR CON LOS Widget Text y Button 5/13----

	-> Text: Se utilizara par introducir texto largo.

	-> Button: Botones para interactuar con la interfaz.
'''

from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=600, height=400)
miFrame.pack()

minombre=SringVar() # Variable que usaremos mas abajo en el uso de un boton

cuadroNombre = Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1)

nombreLabel = label(miFrame, text='Nombre: ')
nombreLabel.grid(row=0, column=0, sticky="e", pady=30)

nombreComentario = label(miFrame, text='Comentarios')
nombreComentario.grid(row=1, column=0)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=1, column=1)

# Aqui estamos creando una barra vertical "yview" en el comando "textoComentario", con
# "Scrollbar". En el "grid", indicamos donde queremos colocar la barra
# Con "sticky='nsew' logramos que la barra se alarge y se pueda desplazar.
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=1, column=2, sticky="nsew")
# Para que el scroll se haga corectamente en la posición de escritura habría que añadir
# la siguiente instrucción al cuadro de texto, despues de la instrucción "scrollVert".
# "y" seguido "scrollcommand", indica la dirección de movimiento vertical.
textoComentario.config(yscrollcommand=scrollVert.set)

# A continuación colocamos un boton en la raiz.
def codigoBoton():
	minombre.set("Juan")
# Con "command" hacemos uso de la función para en este caso imprimir un texto
botonEnvio = Button(raiz, text="Salir", command=codigoBoton)
botonEnvio.pack()