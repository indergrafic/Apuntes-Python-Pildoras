'''
	LOS GENERADORES 

	TEMA 19

	- Son estructuras que extraen valores de una funcion y se almacenan en objetos iterables (que
	se pueden recorrer, con bucles while, for u otros).
	- Estos valores se almacenan de uno en uno.
	- Cada vez que un generador almacena un valor, esta permanece en un estado pausado hasta que 
	se soilicita el siguiente. Esta característica es conocida como "suspensión de estado".

	x Su ventajas son mejor eficiencia
	x Muy útiles con listas de valores infinitos.
	x Bajo determinados escenarios, será muy útil que un generador devuelva los valores de uno en uno.

		SINTAXIS: def nombrefuncion():

						yield numeros -> "valor devuelto" (puede llevar un return)

'''
# Creamos una funcion(de modo return) para generar numeros pares.
# Si la ejecutamos nos dara 9 pares: 2,4,6,8,10,12,14,16,18 y sera generada completa
# y guardada en memoria, con su consiguiente consumo de tiempo y espacio.
def generapares(limite):
	num=1
	milista=[]
	while num<limite:
		milista.append(num*2)
		num +=1
	return milista
print(generapares(10))


# A continuacion el mismo ejemplo pero usando un "generador", retornando con comando "yield".
# Nos ira dando los elementos de la lista de uno en uno a medida que se valla llamando la
# función, comsumiendo pocos recursos en memoria y el menor tiempo posible, haciendo que
# la eficiencia sea mejor.
def generadores(limite):
	num=1
	while num<limite:
		yield num*2
		num+=1
devuelvepares=generapares(10) # Variable que guardara los pares que se vayan generando.
for i in devuelvepares:
	pirnt(i)

# para que nos devuelva valor a valor y no una lista, quitaremos el bucle "for" y en el print
# se usara la funcion "next", que nos dara el valor que se a generaldo en ultimo lugar.
print(next(generapares))



'''
	TEMA 20

	- Nueva instruccion "yield from".
	- Su utilidad: Simplificar el código de los generadores en el caso de utilizar bucles anidados,
	por ejemplo: un for dentro de otro for. Con ello conseguimos acceder al interior de un elemento,
	por ejemplo una lista, y podriamos acceder a la segunda dimension, es decir, a los subelementos
	de la lista.

'''

def devuelve_ciudades(*ciudades): # el * indica que la funcion va ha recivir un numero indeterminado
								  #de elemeentos y que se reciviran en forma de Tupla.
	for elemento in ciudades:
		yield elemento

ciudades_devueltas=devuelve_ciudades("Madrid", 'Barcelona', 'Bilbao')
print(next(ciudades_devueltas))
print(next(ciudades_devueltas)) # Se imprimira Madrid y Barcelona.


# A continuación un ejemplo de como hacceder a los subelementos con bucles anidados.	
def devuelve_ciudades(*ciudades):
	for elmento in ciudades:
		for subElemento in elemento
		yield subElemento
ciudades_devueltas=devuelve_ciudades("Madrid", 'Barcelona', 'Bilbao')
print(next(ciudades_devueltas))
print(next(ciudades_devueltas)) # Se imprimira M y la a de Madrid.

# Ahora se hace lo mismo pero con "yield from" usando solo el primer bucle.
def devuelve_ciudades(*ciudades):
	for elmento in ciudades:
		#for subElemento in elemento (queda eliminado)
		yield from elemento
ciudades_devueltas=devuelve_ciudades("Madrid", 'Barcelona', 'Bilbao')
print(next(ciudades_devueltas))
print(next(ciudades_devueltas)) # Se imprimira M y la a de Madrid.