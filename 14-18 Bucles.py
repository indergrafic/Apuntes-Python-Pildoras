# BUCLES 

	# TEMA 14

		# Bucles Determinados(nº determinado de veces y se sabe cuantas veces se ejecutara).
		# Bucles Indeterminados(nº indeterminado de veces, no se sabe cuantas vecesse ejecutara
		# y nº de veces dependerá de las circunstancias durante la ejecucion del programa)

		# BUCLES DETERMINADOS
		# Bucle "for"
			# SINTAXIS: "for" variable "in" elemento a recorrer ":"
						# Cuerpo del bucle.

for i in [1,2,3]:
	print("Hola")

# Otro ejemplo que funciona igual. Los numero y letras forman el nº de veces que se repetirá.

for i in ["a","b","c"]:
	print("hola")

# En este caso repetira nº de veces igual al nº de elementos pero imprimira el texto de los elementos.

for i in ["a","b","c"]:
	print(i)
	



	# TEMA 15

		# Recorriendo string  -  Tipo range  -  Notaciones especiales con print
		# Los elementos dentro de los corchetes funcionaran como un contador de tepeticiones del print.

for i in ["Pildoras","Informaticas",3]:
	print("Buenas", end="")  # con la funcion "end" se imprimira sin salto de linea.

for i in "juan@pildorasinformaticas.es":
	print("Adios", end="")   # repetira tantas veces como caracteres haya en el elemento a recorrer.

print()

	# Comprovación si dentro del email existe el caracter "@""
email=False
for i in "juan@pildorasinformaticas.es":
	if(i=="@"):
		email=True

if email==True:
	print("E-mail correcto")
else:
	print("E-mail incorrecto")


	# En este caso funciona igual pero con el email introducido.
email=False
miemail=input("Introduce tu E-mail: ")
for i in miemail:
	if(i=="@"):
		email=True

if email==True:
	print("E-mail correcto")
else:
	print("E-mail incorrecto")


	# Usando los condicionales and o or. Y colocaremos un contador para el bucle.
	# -dará errores si se introduce varios puntos o arrobas, abria que mejorar el programa.
contador=0
miemail=input("Introduce tu E-mail: ")

for i in miemail:
	if(i=="@" or i=="."):
		contador=contador+1

if contador==2:
	print("E-mail correcto")
else:
	print("E-mail incorrecto")

	# Uso del tipo "range" en un bucle.

for i in range(5):  # repetira el print 5 veces desde el 0 al 4
	print("Hola")



	# TEMA 16

	# Tipo "range"
	# Anotaciones especiales de "print"

		# Union de texto con variables en el "print"
for i in range(5):
	print(f"valor de la variable {i}")


for i in range(5,10):		# La impresion se realizara desde el 5 hasta el 9
	print(f"valor de la variable {i}")

for i in range(5,50,3):		# El conteo se realizara de 3 en 3 desde el 5 hasta el 50
	print(f"valor de la variable {i}")

	# Uso de la funcion "len" para conocer el nº de elementos dentro de "range"

valido=False
email=input("Introduce tu E-mail: ")

for i in range(len(email)): # Nos dará el valor de caracteres introducidos en el input
	if email[i]=="@":		# Recorrera caracter x caracter "i nº de veces" buscando la "@"
		valido=True

if valido:
	print("E-mail correcto")
else:
	print("E-mail incorrecto")






	# TEMA 17

	# BUCLE "while" (nientras que)

			# Mientras que la condicion se cumpla(verdadera) se irá repitiendo el cuerpo del bucle hasta que 
			# la condicion deje de cumplirse(falsa). Parecido a lo que hace la función "if"

		# SINTAXIS:    "while" condicion :
		#		Cuerpo del bucle


i=1
				# Bucle determinado
while i<=10:	# Repeticion de 10 veces la impresion y saldra del bucle.
	print("ejecucion" + str(i))
	i=i+1

print("Terminó la ejecución")


				# Bucle indeterminado
edad=int(input("Introduce tu edad por favor: "))
while edad<0:	# Seguira dentro del bucle hasta que indiquemos una edad positiva.
	print("Has introducido una edad negativa. Vuelva a introducirla.")
	edad=int(input("Introduce tu edad por favor: "))
	

print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirarnte: " + str(edad))


	# El bucle tiene dos condiciones para tener un rango de edad que introducir.
edad=int(input("Introduce tu edad por favor: "))
while edad<0 or edad>100:	# Seguira dentro del bucle hasta que indiquemos una edad entre 0 y 100.
	print("Has introducido una edad negativa. Vuelva a introducirla.")
	edad=int(input("Introduce tu edad por favor: "))
	

print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirarnte: " + str(edad))


	# Forma de realizar un bucle para que no se convierta en infinito.
import math	# para importrar la funcion "math" y poder hacer la raiz cuadrada.
print("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero por favor: "))

intentos=0	# el numero de intentos sera 3 ya que "0" es el primero "1" el segundo y "2" el tercero

while numero<0:
	print("No se puede hallar la raiz de un número negativo")

	if intentos==2:	# Cuando los intentos sean igual a "2"(el tercer intento), saldra del bucle.
		print("Has consumido demasiados intentos. El programa ha finalizado.")
		break;	# Instruccion que sierve para salir del bucle como parte de la funcion "if"

	numero=int(input("Introduce un numero por favor: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero) # "math.sqrt" instruccion para hayar la raiz cuadrada
	print("La raiz cuadrada de" + str(numero) + "es" + str(solucion))



	# TEMA 18

	# Instrusciones "Continue": Es un salto a la siguiernte interaccón de un bucle
				#	"pass": Devuelve la instruccion "null", como si no ejecutara el bucle.
				#	"else": Su uso es como se hace con un condiconal.

	# CONTINUE

for letra in "Python":
	
	if letra=="h":
		continue 	# Ignora la linea que va a imprimir la letra "h".

	print("Viendo la Letra: " + letra)


nombre="pildoras informaticas"	# En este pequeño programa se imprimira el numero de caracteres,
print(len(nombre))				# pero nos dara 21 ya que contará el espacio en blanco.


nombre="pildoras informaticas"
contador=0						# Para resolverlo, en el siguiente ejemplo se pondra una instruccion
for i in nombre:				# "if" que haga que cuando llege al espacio reseuelva la funcion "continue"
								# y salte su conteo.
	if i==" ":
		continue

	contador +=1
print(contador)

	# PASS

while True:			# La instrucción "pass" serviria en este caso de un bucle infinito salir de él
	pass 			# usando las teclas "Ctrl+c".

class MiClase:		# O para cuando queremos crear una clase que queremos completar mas tarde
	pass 			# y la dejariamos como si no existiera.


	# ELSE

email=input("Introduce tu email, por favor: ")

for i in email:		# El uso de "else" en un bucle es opional, una erramienta mas.

	if i=="@":		# Podemos ver que el "else" no esta identado a este "if" sino al "for."
		arroba=True

		break;		# De modo que si el "if" se cumple se imprimira "True"
					# De otro modo el "break" hará que se salga del bucle.
else:				# En ese ultimo caso, funcionara el "else" y se imprimira "False".
	arroba=False

print(arroba)

