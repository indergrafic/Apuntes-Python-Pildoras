''' PROGRAMACION ORIENTADA A OBJETOS
				"POO"


	TEMA 24

		2 Formas de Programar
			(Paradigmas)

	Programacion 		Programacion
	orientada a 		Orientada a
	procedimientos 		Objetos.

	* P. orientada a procedimientos:
	- Fortran, Cobol, Basic, etc..
	* P. orientada a objetos:
	- Python, Java, C++, etc..

	-> Progamacion Orientada a Objetos <-

	* 	¿En qué consiste?
	- Consiste en trasladar la naturaleza de los objetos de la vida real al
	código de progamación.

	*	¿Cuál es la naturaleza de un objeto de la vida real?
	- Los objetos tienen un estado, un comportamiento,(¿Qué puede hacer?),
	y unas propiedades.

	* 	Pongamos un ejemplo: El objeto Coche.
	- Su estado: puede estar parado, circulando, aparcado, etc...
	- Sus propiedades: color, peso, tamaño, etc...
	- Su comportamiento: arrancar, frenar,acelerar, etc...
	
	* Ventajas:
	- Programas divididos en "trozos", "partes", "módulos" o "clases".
	  Modularización.
	- Muy reutilizable. Herencia.
	- Si existe fall en alguna linea de código, el programa continuará
	con su funcionamiento. Tratamiento de Excepciones.
	- Encapsulamiento.

		* Vocabulario de la POO *
	- Clase.
	- Objeto.
	- Ejemplar de clase. Instancia de clase. Ejemplarizar una clase.
	  Instanciar una clase.
	- Modularización.
	- Encapsulamiento / encapsulación.
	- Herencia.
	- Polimorfismo.


	TEMA 25

	- Que es una Clase: Modelo donde se redactan las caracteristicas
	comunes de un grupo de objetos (chasis o ruedas de un coche).

	- Ejemplar / Instancia o Objeto de clase: Es un objeto o ejemplar
	perteneciente a una clase.

	- Modularización: Una aplicación puede estar compuesta de varias
	clases.

	- Encapsulación: El funcionamiento de una clase nada sabe de otra
	clase y no se podria acceder de una a otra.

	- Metodos de acceso: Es la forma de conectar entre clases pero con
	posibilidad limitada en su acceso.

	** Nomenclatrua del Punto **
	- Si creamos un objeto se le da un nombre.
	Para acceder a las propiedades del objeto desde código, se utiliza
	la Nomenclatura del Punto:
	- Ejm: nombreObjeto.Objeto=
			- nombrePropiedad.Propiedad=


	TEMA 26

	Construcción de una Clase
'''
class Coche():

	# Creamos un "Constructor" de la case Coche:
	# Sintaxis como sigue:
	#__init__ no dice que es el estado "inicial" del objeto.
	# Teniendo que iniciar las variables con la palabra "self."

	def __init__(self): 

	#Algunas posibles Propiedades
		self.largoChasis=250
		self.anchoChasis=120		# Estas caracteristicas indican el "estado inicial"
		self.__ruedas=4				# de nuestro objeto. Se indicaria con un "Contructor"
		self.__enmarcha=False		# Con los dos "__" encapsulamos las variables.

	#El comportamiento (Creacion de Métodos)
	# Un "Metodo" es una funcion perteneciente a una clase
	def arrancar(self):
		self.__enmarcha=True

	def estado(self):
		if(self.__enmarcha):
			return 'El coche esta en marcha'
		else:
			return 'El coche esta parado'

miCoche=Coche() #Instanciar/ejemplarizar una clase.

print('el largo del coche es ', miCoche.largoChasis)
print('el coche tiene', miCoche.ruedas, 'ruedas')
miCoche.arrancar()

print(miCoche.estado())



	# TEMA 27

''' -> Creacion de un segundo objeto.
	-> Proporcionar el "estado inicial" del objeto. Método "__init__"
	-> Encapsulación (se trataría de, no permitir el cambio de las caracteristicas o constructor de 
		nuestro objeto desde fuera de la clase). Hariamos uso de la colocación de dos "__" en la variable
		que queremos encapsular.
'''

print('----------------A continuación creamos el segundo objeto--------------------------')

miCoche2 = Coche()

print('el largo del coche es ', miCoche2.largoChasis)
print('el coche tiene', miCoche2.ruedas, 'ruedas')
print(miCoche2.estado())

# Modificacion del "Metodo" o función anterior perteneciente a la clase "Coche".
# Abria que sustituir este codigo por el anterior, quedando así:

def arrancar(self,acarrancamos):
	self.__enmarcha = acarrancamos

	if (self.__enmarcha):   # De esta forma indicamos se es "True"
		return 'El coche está en marcha'
	else:
		return 'El coche esta parado'

def estado(self):
	print('El coche tiene', self.__ruedas, 'ruedas. Un ancho de ', self.anchoChasis, ' y un largo de',
		self.largoChasis)

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()



	# Tema 28

''' -> Encapsulación de métodos:
		+ ¿Qué es?
			Se trataria de hacer inapcesible un metodo desde fuera de la propia clase.
			Colocariamos en el nombre del metodo dos "__"(ejem: __chequeo_interno)
			
		+ ¿Por qué utilizar la encapsulación?
			Se sutilizará a razon de nuestras necesidades y del comportamiento que queramos
			que tenga nuestro objeto.

		Acontinucación un ejemplo que se podria añadir a la clase creada al inicio:
'''

def __chequeo_interno(self):
	print('Realizando chequeo interno')

	self.gasolina = 'ok'
	self.aceite = 'ok'
	self.puertas = 'cerradas'

	if(self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas'):
		return True
	else:
		return False

def arrancar(self, acarrancamos):
		self.__enmarcha = acarrancamos

		if(self.__enmarcha):
			chequeo = self.__chequeo_interno()

		if (self.__enmarcha and chequeo):   
			return 'El coche está en marcha'
		elif(self.__enmarcha and chequeo == False):
			return 'Algo ha ido mal en el chequeo, no se puede arrancar'
		else:
			return 'El coche esta parado'



'''	TEMA 29

	--HERENCIA--

-> Con la Herencia se traslada el comportamiento normal humano a codigo, heredando caracteristicas,
	comportamientos y/o atributos.
	Ejemplo:

			Abuelo							Clase1 (Clase Padre o Superclase)

			Hijo							Clase2 (Subclase de Clase1 o Superclase de otras clases)
		
	Nieto1 - Nieto2 - Nieto3		Clase3 - Clase4 - Clase5

+ En este ejemplo el Hijo heredara caracteristicas, comportamientos, etc..., del Abuelo, y a su vez los
	Nietos, heredaran tanto del Abuelo como del Padre.

-> Para reutilizar código en caso de crear objetos similares.

	..SINTAXIS..
'''
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

''' -> A continuacion creamos una Clase que va ha "Heredar" todas las caracteristicas de la clase
Vehiculos. 
->Para ello cuando creamos dicha clase Moto, introducimos dentro de los parentesis la clase
de la que hereda '''

class Moto(Vehiculos):
	pass

miMoto=Moto('Honda', 'CBR')

miMoto.estado()


'''	TEMA 30

	-- HERENCIA II --

* Sobre escritura de métodos
* Herencia simple y múltiple

	---Continuando con el ejemplo anterior, añadimos comportamientos a la case Moto:
'''
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

class Moto(Vehiculos): #Estamos creando un comportamiento(caballito) a la moto.
	hcaballito=''
	def caballito(self):
		self.hcaballito='Voy haciendo el caballito'
	def estado(self):
		print('Marca: ', self.marca, '\nModelo: ', self.modelo, '\nEn Marcha: ', self.enmarcha,
			'\nAcelerando: ', self.acelera, '\nFrenado: ', self.frena, self.hcaballito)

miMoto=Moto('Honda', 'CBR')
miMoto.caballito
miMoto.estado()

