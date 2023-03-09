'''
	.:TEMA 21:.

	Las EXEPCIONES I

	-> Las exepciones son errores que ocurren duante la ejecución del programa.
	La sintaxis del código es correcta pero durante la ejecución ha ocurrido "algo inesperado".
'''

def divide(num1,num2):
	return num1/num2

'''
	-> Si usamos la anterior funcion y quisieramos dividir un numero por cero se producirá un error,
	ya que ese tipo de divisiones son infinitas, aunque no existe ningun herror de sintaxis o de otro 
	tipo.Para ello hacemos uso de una "CAPTURA O CONTROL DE EXEPCION".

	-> Este tipo de errores de ejecución se pueden controlar para que la ejecución del programa
	continúe. Es lo que se conoce como "manejo o control de excepciones".

	-> Debemos en ese caso declarar un "Bloque-> try - except".
	1- Declaramos la función "try", con antelación al "return" que produce el error.
	2- A continuación indicamos la excepción determinada "ZeroDivisionError" en este caso.
	3- Y declaramos despues si queremos, lo que indicaria si el error se produce, ademas
	de lo que nos devolveria la función con el 'return'.
'''

def divice(num1,num2):
	try:
		return num1/num2
	except ZeroDivisionError:
		print ('No se puede dividir entre 0')
		return 'Operación errónea'

'''
	Si la excepcion indicada no se produce, pero existe la posibilidad de que en el mismo apartado
	de código se produzca otro error, este, hará que el programa caiga, saltandose la exepción.
'''


'''
	TEMA 22

	-> Captura de Varias Excepciones y uso de la instrucción "finally".

	-> En el ejemplo siguiente como en el anterior no hay errores de sintaxis, sin embargo
	si introducimos en la division un cero o un texto el programa cae y no se resolveria,
	ni todo cuanto haya despues. Para evitar esto metemos todo el bloque dentro de un
	"try - except", en el cual podemos unir varios "except".

'''
def divide():
	op1 = (float(input('Introduce el primer numero')))
	op2 = (float(input('Introduce el segundo numero')))
	print('La division es: ' + str(op1/op2))
	print('Calculo Finalizado')
divide()

	# Con Varios "Except":
	# Opcionalmente se puede usar un "else" tras un "except", que se ejecutara
	# siempre que no se produzca una exepción.

def divide():
	try:
		op1 = (float(input('Introduce el primer numero')))
		op2 = (float(input('Introduce el segundo numero')))
		print('La division es: ' + str(op1/op2))
	except ValueError:
		print('El valor introducido es erróneo')
	except ZeroDivisionError:
		print('No se puede divicir por 0!')
	else:
		print('Todo correcto')
	
	print('Calculo Finalizado')
divide()

'''
	-> El siguiente ejemplo se trata de englobar el bloque en un "except" generico.
	No es muy recomendado ya que no se especifica el tipo de error, solo conseguimos
	que no caiga el progrma.
	-> Ademas se incluye la instrucción "finally", que hace que la instrucción posterior
	se ejecute siemmpre, se produzca un error o no.
'''
def divide():
	try:
		op1 = (float(input('Introduce el primer numero')))
		op2 = (float(input('Introduce el segundo numero')))
		print('La division es: ' + str(op1/op2))
	except:
		print('Ha ocurrido un error')
	finally:
		print('Calculo Finalizado')
divide()


'''
	TEMA 23

	-> Lanzamiento de excepcones.
		Donde nosotros provocamos las exepciones cuando ocurra algo en nuesto codigo.

		-> Utilizaremos la instrucción "Raise".
		-> La intrucción "raise" nos permitira crear excepciones propias(mas adelante
			cuando vamos la POO)

	Si en el siguiente ejemplo introducimos un numero negativo, aunque no se produce un
	error, daria un resultado extraño. Para evitarlo se realizaria lo siguiente:
'''
def evaluaEdad(edad):
	if edad < 20:
		return 'Eres muy joven'
	elif edad < 40:
		return 'Eres joven'
	elif edad < 65:
		return 'Eres maduro'
	elif edad < 100:
		return 'Cuidate...'

print (evaluaEdad(18))

'''
	Ya restificado, con un lanzamiento de error(usando un error cualquiera).
	Podriamos crear una clase de error para que el error indicado ralize lo que 
	nosotros consideremos.
'''
def evaluaEdad(edad):
	if edad < 0:
		raise TypeError('No se permite una edad negativa')

	if edad < 20:
		return 'Eres muy joven'
	elif edad < 40:
		return 'Eres joven'
	elif edad < 65:
		return 'Eres maduro'
	elif edad < 100:
		return 'Cuidate...'

print (evaluaEdad(18))

'''
	En el siguiente programa creamos un tipo de error con "raise" que lanza un mensaje 
	si se cumple una condición, y mas adelante usamos la funcion 'try - except' donde
	ademas daremos nombre a la excepción capturada, y ejecutara el "raise" anterior,
	haciendo que el programa no caiga y nos informe del error producido.
'''

import math

def caldulaRaiz(num1):
	if num1 < 0:
		raise ValueError ('El número no puede ser negativo')

	else:
		return math.sqrt(num1)

op1 = (int(input('Introduce un número: ')))

try:
	print(caldulaRaiz(op1))

except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)
	
print('Programa terminado')