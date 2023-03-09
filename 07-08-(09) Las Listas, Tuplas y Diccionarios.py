		# TEMA 7

	# LAS LISTAS

	# Estructura de datos que nos permite almacenar gran cantidad de
	# valores (equivalente a los "array" en otros lenguajes de programación)

	# En Python las listas pueden guardar diferente tipo de valores
	# no asi en otros lenguajes, con los array.

	# Se pueden expandir dinámicamente añadiendo nuevos elementos
	# (otra novedad respecto a los arrays en otros lenguajes)

	# SINTAXIS:
	# 					 nombreLista=[elem1,elem2,elem3...]
	# El indice empieza con el elemento 0    1     2   etc
	# Dentro de la lista puede haber todo tipo de elementos diferentes o no.

milista=["maria","pepe","marta","antonio"]
print(milista[:]) #imprime la lista completa
print(milista[2]) #si contamos por el indice 2 sera marta que esta en posición 3
print(milista[-2]) #en negativo empieza a contar al reves desde -1 que es antonio
print(milista[0:3]) #imprime todo los nombre entre cero y 3, escluyendo el 3
print(milista[:3]) # este ejmplo es igual pero sin el cero
print(milista[1:]) # se accede a los elemento desde el número indicado hasta el final

# La funcion "len" nos dara el nº de elementos dentro de la lista
print(len(milista))

# para agregar mas elementos al final de la lista, añadir .append
milista.append("sandra")
print(milista[:])

# para agregarlos de forma intermedia, añadir .insert
milista.insert(2,"pedro") # el nº 2 indica el lugar donde se insertara lo que
print(milista[:])	# haya despues de la ","

# Para agregar varios elementos a la lista desde el final, añadir .extend
milista.extend(["alverto","joaquin","jorge"])
print(milista[:])

# Uso de un operador que realiza una funcion parecida a .extend
milista2=[8,7]
milista3=milista+milista2
print(milista3[:])

# Devolucion del indice dentro de una lista. Si dentro de la lista existen dos elementos
# iguales devuelve el primer elemento de la lista, con .index
print(milista.index("sandra"))

# Instrución para saber si un elemento se encuentra dentro de la lista, con in
print("pepe" in milista) # nos dara "True" o "False", se encuentre o no.

# Para eliminar un elemento de la lista, usamos .remove
milista.remove("antonio")
print(milista[:])

# Para eliminar el último elemento de una lista, usaremos ".pop"
milista.pop()	# Si indicamos el nº indice "(2)", eliminara el elemento en ese indice.
milista.pop(2) 
print(milista[:])

#Para eliminar un elemento conocido usaremos ".remove"
milista.remove("pepe")

# Para borrar todos los elementos usamos ".clear"
milista.clear()

# Para hacer que la lista se de la vuelta a los elementos usaremos ".reverse"
milista.reverse()

# Para ordenar la lista de menor a mayor(en especial para numeros) usamos ".sort"
milista.sort() 

# Para ordenar la lista de mayor a menor(en especial para numeros) usamos ".sort"
milista.sort(reverse=True)	# y entre parentesis "reverse=True"

# Metodo ".count" para conocer cuantos elementos hay iguales en la lista.
print(milista.count("pepe"))



#Operador para repetir la lista tantas veces como necesitemos, añadiendo * y la cantidad
milista2=[8,7]*3
print(milista2[:])






		# TEMA 8

	# TUPLAS


# Son listas inmutables, ya que no pueden ser modificadas como con las listas.
	# No podremos hacer uso de (append, extend,remove,etc..).
	# Si podremos extraer porciones, pero se convertiran en una nueva tupla.
	# Desde la version 3 si podremos hacer busquedas (index).
	# Si permiten comprobar si un elemento se encuentra en la tupla con "in" (true o false).

# Su utilidad respecto a las listas:
	# Mas rapidas.
	# Menos espacio en memoria (mayor optimizacion)
	# Formatean String.
	# Pueden utilizarse como claves en un diccionario. (las listas no)

	# SINTAXIS:
	# nombreTupla=(elem1,elem2,elem3,...) #Es conveniente poner los parentesis pero no son obligatorios.
#    posición       0     1     2    etc...


# Ejercicios

mitupla=("Pepe", 12,2,2022)
print(mitupla) # A diferencia de las lista la impresion la hace entre parentesis y no entre corchetes.

print(mitupla[1]) # Nos imprimirá el elemento en la posición del indice indicado.

milista=list(mitupla) # Hemos convertido la tupla en una lista, con el comando "list".
print(milista) # La imprimirá entre corchetes ya que se ha convertido en una lista.

mitupla1=tuple(milista) # Convertimos la lista en tupla, con "tuple".
print(mitupla1) # Comprovamos que imprime parentesis de la tuplas y no los corchetes de las listas.

print("Pepe" in mitupla1) # "in" lo usaremos para comprobar si un elemento se encuentra dentro de la tupla
						  # dando como resultado un "true" o un "false".

print(mitupla1.count(12)) # El comando ".count(elemento)", nos proporciona el numero de veces que se repite
						  # dicho elemento dentro de la tupla. Será 1 en este caso.

print(len(mitupla1)) # "len" nos proporciona el numero de elementos que componen la tupla. 4 en este caso.

mitupla2=("Andres",) # Estamos creando una tupla con un solo elemento, pero no hay que olvidarse de poner
					 # una "coma" despues del elemento.
print(len(mitupla2)) # nos dara la longitud de la tupla que es 1.

mitupla3="Juan",13,1,1995 # Cuando no lleva parentesis se le denomina "Empaquetado de tupla"
print(mitupla3) # La imprimira igual con parentesis.

	# Desempaquetado de tupla, es asignar por orden a las variales los elementos de la tupla.

nombre,dia,mes,agno=mitupla3
print(nombre)
print(dia)
print(mes)
print(agno)
# o
print("Nombre=",nombre)
print("Dia=",dia)
print("Mes=",mes)
print("Año=",agno)

	# Para convertir Ejm 1º: Tuplas en Lista y Ejm 2º:Listas en Tuplas.
	lista = list(tupla)
	tupla = tuple(lista)





			# TEMA 9

	# DICCIONARIOS


# Qué son los Diccionarios:
"""	- Son estructuras de datos que nos permite almacenar valores de diferente
	tipo (enteros,cadenas de texto, decimales) e incluso listas, tuplas y otros
	diccionarios.

	- La principal cracteristica de los diccionarios es que los datos se almacenan
	(clave:valor) para cada elemento almacenado.

	- Los elementos almacenados no estan ordenados. El orden es indiferente a la
	hora de almacenar información en un diccionario.

	SINTAXIS:  midiccionario={elementos clave:valor}"""


# Ejemplos:

midiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}
print(midiccionario) # LLamamos a la impresion del Dicconario.

print(midiccionario["Francia"]) # Para llamar una clave y nos imprima su valor.
								# Pero no se puede llamar a un valor, pues nos daría error.

midiccionario["Italia"]="Lisboa" # Para añadir un elemento al diccionario. ( este ejemplo
								 # tiene un error intencional para solucionarlo posteriormente)
print(midiccionario)

midiccionario["Italia"]="Roma" # Corregimos el anterior error ya que lo que hacemos es sobreescribir.
print(midiccionario)

del(midiccionario["Reino Unido"]) # Método para eliminar un elemento del diccionario.
print(midiccionario)

	# Diccionario con diferentes Claves:Valor.
midiccionario1={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(midiccionario1)

	# Uso de una Tupla para almacenar las Claves de un diccionario.
mitupla=["España", "Francia", "Reino Unido", "Alemania"]
	# y asignarle valores en un dicciconario.
midiccionario2={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres", mitupla[3]:"Berlin"}
print(midiccionario2)

print(midiccionario2["Francia"]) # Imprimimos el valor de la clave llamada (Francia en este caso). Nos daria Paris.

	# Podemos incluir dentro de un diccionario una Tupla. (Anillos es la Tupla)
midiccionario3={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionario3)
print(midiccionario3["Anillos"]) #nos imprime su valor que es todos los datos entro de la tupla.

	#Incluso podemos introducir un diccionario entro de otro y una tupla dentro de un diccionario.
	# 1er. diccionario-"midicconario4", 2do. diccionario-"Anillos", y 3ro. la tupla-"Temporadas"
midiccionario4={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario4["Anillos"]) # Impresion del diccionario "Anillos" que ademas es una Clave:Valor

print(midiccionario4)

print(midiccionario4.keys()) # Usar "Keys()" para que nos imprima las Claves del diccionario indicado.

print(midiccionario4.values()) # Usando "Values()" nos imprimira los Valores del diccionariol.

print(len(midiccionario4)) # Con "Len()" nos informamos del número de elementos que componen el diccionario.

print(midiccionario4.items()) # Nos ofrece la impresion en tuplas de las claves:valor de mi diccionario.

print.clear() # Para borrar todo el diccionario creado. Entre() indicar nombre del diccionario.

	# CLAVE NO EXISTENTE
	# Si queremos que a la hora de buscar un valor con una clave equivocada no nos salga
	# un mensaje de error por parte de Python, usaremos esta forma:
	print(midiccionario4.get(3,"No existe ese dato en mi diccionario."))
	# Hay que usar ".get()" despues de la clave usamos "," y despues el mensaje que queramos
	# y que hos sirva para explicar que no se encuenra dicha clave.