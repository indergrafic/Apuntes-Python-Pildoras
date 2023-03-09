"""
	* TEMA 51

	------------INTERFAS GRAFICA------------

	--> Botones de Selección. "CheckButtons"

	Botones de selección para preguntas de respuesta multiple.

	Creación de una interfas para selecionar entre tres opciones de viajes.
"""

from tkinter import *

raiz = Tk()

raiz.title("Ejeimplo")

playa = IntVar()
monatana = IntVar()
turismoRural = IntVar()

def opcionesViaje():

	opcionEscogida = ""

	if(playa.get() == 1):
		opcionEscogida += " -Playa-"
	if(monatana.get() == 1):
		opcionEscogida += " -Montana-"
	if(turismoRural.get() == 1):
		opcionEscogida += " -Turismo Rural-"

	textoFinal.config(text=opcionEscogida)

foto = PhotoImage(file="avion.png")
Label(raiz, image=foto).pack()

frame = Frame(raiz)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=monatana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame, fg="red")
textoFinal.pack()

raiz.mainloop()


"""
	* TEMA 52

	------------INTERFAS GRAFICA------------

	--> Barras de Menús, en la parte superior.

	Con opciones de sub-mençu

	Creación de una interfas con opciones de: Archivo, Edición, Ayuda
"""

from tkinter import *
from tkinter import messagebox

raiz = Tk()

# ---> Funcion para crear la caja de información. Hay darle dos parametros. 1- Nombre de la caja y 2- Info interior.
def infoAdicional():
	# Ventana de Info
	messagebox.showinfo("Información", "Practicas Tkinter 2023")
	
def avisoLicencia():
	# Ventana de Aviso
	messagebox.showwarning("Licencia", "Producto bajo licencia 2000")

def salirAplicacion():
	# Ventana opciones de Salir de la aplicación. Hay que darle funcionalidad.
	# El Metodo askquestion proporciona dos valores, "yes" y "no".
	# ---> Con el metodo askokcancel cambia los botones a "aceptar" y "cancelar", devolviendo "True" o "False"
	valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
	if valor == "yes":
		raiz.destroy()

def cancelarGuardar():
	# ---> Con el metodo askokcancel cambia los botones a "aceptar" y "cancelar", devolviendo "True" o "False"
	opcion = messagebox.askokcancel("Guardar", "¿Desea Guardar Archivo?")
	if opcion == True:
		raiz.destroy()

def cerrarDocumento():
	opcion = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento Bloqueado")
	if opcion == False:
		raiz.destroy()

#Creacion del menú
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

#Componentes que formaran el menú --> El "tearoff=0" es para quitar la barra de lineas superior de cada opción.
archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar", command=cancelarGuardar)
archivoMenu.add_command(label="Guardar Como")
# Instrucción "add_separator" para que aparezca una linea de separación
# Debe ir por debajo de la linea que queremos dividir.
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion = Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

# Aqui no le hemos quitado las lineas superiores con "tearoff"
archivoHerramientas = Menu(barraMenu)
archivoHerramientas.add_command(label="Efectos")
archivoHerramientas.add_command(label="Filtros")

archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de", command=infoAdicional) # --->El command es para que funciones la caja de Info.


# Componentes del Menu Superior.
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

raiz.mainloop()




"""
	* TEMA 53

	------------INTERFAS GRAFICA------------

	--> Ventanas modales para informar, avisar

	o permitir realizar tareas al usuario.

	-> Para usar estas ventanas hay que importar su propia libreria ya que no se incluye en Tkinter.

			---- "from tkinter import messagebox" ----

	-----> Los ejemplos estan implementados dentro del anterior programa.
	
"""

"""
	* TEMA 54

	------------INTERFAS GRAFICA------------

	--> Ventanas emergentes. Abrir archivos

	-> Para usar estas ventanas hay que importar su propia libreria ya que no se incluye en Tkinter.

			---- "from tkinter import messagebox" ----

	-----> Los ejemplos estan implementados dentro del anterior programa.
	
"""

from tkinter import *
from tkinter import filedialog # Libreria para Abrir Archivos


raiz = Tk()

def abreFichero(): # + info: http://pythonspot.com/tk-file-dialogs/

	fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros Excel", "*.xlsx"),
		("Ficheros Texto","*.txt"), ("Todos los Fiecheros", "*.*")))
	print(fichero)

Button (raiz, texto="Abrir Fichero", command=abreFichero).pack()

root.mainloop()


