# FUNCIONES
			# TEMA 5

	#Conjunto de lineas de código agrupadas que funcionan como una unidad
	#realizando una tarea especifica.

	#Pueden en python devolver valores.

	#Pueden tener parámetros/argumentos.

	#Tambien se las denomina "metodos" cuando se encuentran 
	#definidas dentro de una clase.

	#¿Para qué?
	# Reutilización de código.

	# SINTAXIS de una funcion: def nombre_función(parametros o no):
	# Opcionalmente puede llevar una instruccion: "return"

print("Estamos aprendiendo python")
print("Estamos instrucciones básicas")
print("Poco a poco vamos avanzando")

#Si no queremos compiar un nº de veces lo anterior podemos utilizar una función.

def mensaje(): #declaracion de la funcion
	
	print("Estamos aprendiendo python")
	print("Estamos instrucciones básicas") #Cuerpo de la funcion (las 3 lineas)
	print("Poco a poco vamos avanzando")

mensaje() # llamada de la funcion

# La funcion se puede llamar tantas veces como queramos y entre medias habrá un sin
# número de lineas de código.

print("Esto es un ejemplo de linea de código intermedio")

mensaje()



		# TEMA 6

# Parametro dentro de las Funciones

def suma(): #esto es un ejemplo con el capitulo anterior.
	num1=5
	num2=7
	print(num1+num2)

suma()

	#Ejemplo con parametros dentro de la fución.
def suma2(num1,num2):  # Entre los () van los PARAMETROS.
	print(num1+num2)
# Los parametros se almacenaran de forma correlativa y si llamamos a la
# funcion los parametros tendran que ir en el mismo orden que en la funcion: 5 num1 y 7 num2.
suma2(5,7) # Aqui los numeroS tre los () se denominan ARGUMENTOS. 
suma2(2,3)  
suma2(35,358)
# Cuando llamemos a la funcion podemos indicar de cualquier orde los parametros y añadirles
# cualquier argumento, como se refleja abajo.
suma(num2=12, num1=3)

# Instrucción "return" dentro de una función.

def suma3(num1,num2):
	resultado=num1+num2
	return resultado

print(suma3(2,4))

print(suma3(7,3))

almacena_resultado=suma3(3,17)
print(almacena_resultado)

#Python pasa siempre los resultados como "referencia".


# Argumentos por "Valor" o por "Referencia".
#	Arg. por Valor son variables como enteros, boleanos, complejos, etc..
#	Arg. por Referencia son las variables como cadenas, listas, tuplas, diccionarios, etc..

# Ejm. Argumento por "Valor": (el valor de la variable no cambia nunca)
def doblar_valor(numero):
	numero *= 2
n=5
# En este caso pasamos como argumento una copia del valor al parametro, puesto que en el
# parametro "numero" se va a guardar "5" que es el valor.
doblar_valor(5) 

# Ejm. Argumento por "Referencia":
fef doblar_valor(numeros):
for i,n in enumerate(numeros):
	numeros[i] *=2
n=[5,10,15,20] 
doblar_valor(n)
# En caso de que queramos pasar por valor una colección:
doblar_valor(n[:]) # <- [:]

# Toda las coleccones, listas, conjuntos, diccionarios, etc...; se pasan Argumentos por "Referencia"