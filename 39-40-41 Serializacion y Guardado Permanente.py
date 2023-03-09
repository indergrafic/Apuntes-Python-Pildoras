'''
	* TEMA 39

	---- SERIALIZACION ----

	-> Serialización de Colecciones.

	Se trata de guardar en un fichero externo una Coleccion, un Diccionario o un Objeto.
	Pero con la particularidad que este fichero estará "codificado en binario".
	Codificarlo en binario tene como utilidad por ejemplo, su facilidad para enviarlo
	por internet mas rapidamente, para guardarlo en un disco externo o en una base de datos.

	Para ello debemos usar la biblioteca "Pickle".
		-> Método dump(): volcado de datos al fichero binario externo.
		-> Método load(): carga de los datos del fichero binario externo.

'''
	# Guardar información en un archivo externo.

import pickle

lista_nombres = ["pedro", "ana", "Maria", "isabel"]

fichero_binario = open("lista_nombres", "wb") # "wb" = write y binario

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del (fichero_binario) # Con esta funcion borramos de la memoria el fichero.


	# Para leer el archivo guardado lo leremos de la siguiente forma:

import pickle

fichero = open("lista_nombres", "rb") # "rb" = escritura y binario

lista = pickle.load(fichero)

print(lista)


'''
	* TEMA 40

	-> Como Serializar Objetos.
	

'''	
import pickle


class Vehiculos():

	def __init__(self, marca, modelo):

		self.marca= marca
		self.modelo= modelo
		self.enmarcha= False
		self.acelera= False
		self.frena= False

	def arrancar(self):
		self.enmarcha= True

	def acelerar(self):
		self.acelerar= True

	def frena(self):
		self.frena= True

	def estado(self):
		print('Marca: ', self.marca, '\nModelo: ', self.modelo, '\nEn Marcha: ', self.enmarcha,
			'\nAcelerando: ', self.acelera, '\nFrenado: ', self.frena)

coche1=Vehiculos("Seat", "Leon")
coche2=Vehiculos("Mazda", "MX5")
coche3=Vehiculos("Renault", "Megane")

coches=[coche1, coche2, coche3]

fichero=open("losCoches", "wb")

pickle.pump(coches, fichero)

fichero.close()
del (fichero)

ficheroApertura=open("losCoches", "rb")

misCoches=pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches:
	print(c.estado())


'''	Si la lectura la hacemos en un archivo distinto nos dará error ya que no encontraria la clase Vehiculos.
Para ello habria que volver a copiar la Clase en ese archivo como sigue: '''

import pickle


class Vehiculos():

	def __init__(self, marca, modelo):

		self.marca= marca
		self.modelo= modelo
		self.enmarcha= False
		self.acelera= False
		self.frena= False

	def arrancar(self):
		self.enmarcha= True

	def acelerar(self):
		self.acelerar= True

	def frena(self):
		self.frena= True

	def estado(self):
		print('Marca: ', self.marca, '\nModelo: ', self.modelo, '\nEn Marcha: ', self.enmarcha,
			'\nAcelerando: ', self.acelera, '\nFrenado: ', self.frena)

ficheroApertura=open("losCoches", "rb")

misCoches=pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches:
	print(c.estado())


'''
	* TEMA 41

	---- GUARDADO PERMANENTE ----

	- Se trata de guardar datos de forma permanente en ficheros.
'''

import pickle

class Persona:
	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona nueva con el nombre ", self.nombre)


	def __str__(self):	# Metodo para convertir en cadena de texto un objeto.
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

	personas=[]

	def __init__(self):
		listaDePersonas=open("ficheroExterno", "ab+")
		listaDePersonas.seek(0) # Posicionar el puntero en el inicio.

		try:	# Indicamos que si puede que ejecute lo siguiente y si no, pasa a la excepción.
				self.personas=pickle.load(listaDePersonas)
				print("Se cargaron {} personas al fichero externo".format(len(self.personas)))
		except:	# Se crea un a exepcion para no dar error al inicio cuando no hay personas guardadas.
			print("El fichero esta vacio")
		finally:	# El finally se ejecuta si o si para cerrar la lista y la borre.
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("ficheroExterno", "wb")
		pickle.dump(self.personas, listaDePersonas) # Volcado de información.
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarInfoFicheroExterno(self):
		print("La informacion del fichero externo es la siguiente:")
		for p in self.personas:
			print(p)

miLista=ListaPersonas()

persona=Persona("Sandra", "Femenino", 29)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()