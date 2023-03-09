'''
	* MODULOS

	---- TEMA 34 ----

- ¿Qué son?
	Son un archivo con extensión .py .pyc (Python compilado) o archivo escrito en C
	para CPython, que posee su propio espacio e nombres y que puede
	contener variables, funciones, clases e incluso otros módulos.

- ¿Para qué sirven?
	Para organizar y reutilizar el código (modularización y reutilización)

- ¿Comó se crea un módulo?
	Tan sencillo como crear un archivo con extensión .py (o .pyc o archivo C)
	y guardarlo donde nos interese.


** Para hacer uso de la Modularización hariamos los siguiente:
	1- Crear una carpeta donde irían los archivos con código para usar.
	2- En el nuevo archivo utilizamos la llamada al código mediante (import)
	   o (from nobre_archivo import *).

En el siguiente ejemplo simulamos que tenemos un archivo .py donde hemos
realizado varias funciones que suman, restan y multiplican, llmada "funci_matematicas".
'''
#	El problema de este ejm. es que por cada operación habría que llamar a la función.

import funci_matematicas

funci_matematicas.suma(7, 3)
funci_matematicas.resta(12, 3)
funci_matematicas.multiplica(2, 3)

#	Otro metodo para llamar a las funciones una sola vez mientras las necesitemos
#   utilizar en nuestro código.

from funci_matematicas import suma # (o cambiar por "resta", o "multiplica")

suma(7, 3)
resta(12, 3)
multiplica(2, 3)

#	A continuación un método en el que se haría una única llamada
#	para hacer uso completo del archivo importado, usando un '*'.

from funci_matematicas import * 

suma(7, 3)
resta(12, 3)
multiplica(2, 3)

'''
	La lógica para usar la primera opción o la segunda, es usar solo 
	aquello que necesitamos, para que sea más optimo el uso de memoria.
	Si utilizamos la última, haríamos uso de más recursos en memoria.
'''




'''
	* TEMA 35

	---- PAQUETES ----


1- ¿Qué son?
	Directorios o carpetas conde se almacenarán módulos relacionados entre sí.

2- ¿Para qué sirven?
	Para organizar y reutilizar los modulos.

3- ¿Comó se crea un paquete?
	Tan sencillo como crear una carpeta con un archivo __init__.py.
	Dentro de esa carpeta se guardaran los archivos con las funciones, classes, etc.
	para reutilizar.
	Tambien se puede, del mismo modo, crear subcarpetas para ordenar diferentes archivos
	incluyendo en ellas tambien un archivo __init__.py.
'''

'''
->	De esta forma llamariamos al paquete: (habriamos crado anteriormente una carpeta llamada
	calculos, dentro el archivo __init__.py y el archivo(modulo) "calculos_generrales"con las 
	funciones, suma, resta, etc...)
'''
from calculos.calculos_generales import suma # (o * para hacer uso de todas)

suma(3,2)


'''
->	Su se hubieran creado varias carpetas, ejm: basicos y potencia, dentro de la inicial
	calculos, con sus respectivos archivos(modulos), la forma de llamarlos sería de la misma forma
	indicando su destino con . .
'''
from calculos.basicos.operaciones_basicas import suma # (o * para hacer uso de todas)
# o
from calculos.potencia.redondea_potencia import redondear # (o * para hacer uso de todas)



'''
	* TEMA 36

	---- PAQUETES DISTRIBUIBLES ----


	¿Comó crear Paquetes distribuibles?
	Con ello podriamos inslar los paquetes para que funciones desde cualquer lugar de
	nustro ordenador.

	1- Crear el paquete.
	
	-> Creariamos un archivo "setup.py" que contendría una descripción del paquete vamos
	a distribuir. Tomando como ejemplo lo anterior:
'''
from setuptools import setup

setup(

	name="paquetescalculos", 			#
	version="1.0",						# Estos importantes
	description="Paquete de calculos",	#
	author="Luis",
	author_email="inder@hotmail.com",
	url="www.mates.com",
	packages=["calculos", "basicos.operaciones_basicas"] # Fundamental.
	)
'''
	Despues de crar el archivo "setup.py", tenemos que crear un archivo instalable.
	Desde el Simbolo del sistema por ejemplo y dento de la carpeta del archivo:
	
	-> python setup.py sdist

	2- Instalar el paquete.

	-> Para instalarlo tras descargar y descomprimir, nos iriamos de nuevo al simbolo
	del sistema, nos metemos en la carpeta "dist" y ponemos lo siguiente:

		*-> pip3 install paquetecalculos.1.0.tar.gz

	-> Para desinstalar el paquete cuando queramos, nos iriamos al simbolo de sistema
	y desde cualqueir carpeta indicamos:

		*-> pip3 unistall paquetecalculos

'''