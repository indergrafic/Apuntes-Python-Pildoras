'''
	* ARCHIVOS EXTERNOS

	---- TEMA 37 ----

-> Cómo trabajar con ficheros externos de texto con el modulo "io".

	-> Su objetivo es: persistencia de datos.
	-> Dos alternativas:
	
		-> Manejo de archivos externos.

		Las Fases necesarias para guardar información en archivos externos:

		1-Creación	2-Apertura	3-Manipulación	4-Cierre

		Ejemplo de las fases:
'''
		from io import open

		archivo_texto = open("archivo.txt", "w") # Creación y apertura en modo escritura.

		frase = "Estupendo dia para estudiar Python." # Manipulación.

		archivo_texto.write(frase)					  # Podriamos usar "writelines(lista)" para escribir listas.

		archivo_texto.close()	# Cierre
	# ----------------------------------------------------------------------------------

		from io import open

		archivo_texto = open("archivo.txt", "r") # Creación y apertura en modo lectura.

		texto = archivo_texto.read()  # Si a este metodo "read" le indicamos un nº nos leera solo
									  # a partir del caracter indicado ejm: archivo_texto.read(12).

		archivo_texto.close()	# Cierre

		print(texto)

		# Uso de "readlines" para leer el texto y convertirlo en una lista linea a linea.
		# Con posibilidad de manejarlo como cuarquier otra lista.

		lineas_texto = archivo_texto.readlines() # Manipulación.

		archivo_texto.close()	# Cierre

		print(lineas_texto[:])

	# ---------------------------------------------------------------------------------

		from io import open

		archivo_texto = open("archivo.txt", "a") # Creación y apertura en modo añadir lieneas como "append".

		texto = archivo_texto.write("\nsiempre es una buena ocasión para estudiar Python.") # Manipulación.

		archivo_texto.close()	# Cierre

		# Si comprobamos el archivo de texto creado, ".txt", se habra añadido la frase.

'''
	-> Trabajo con BBDD(base de datos).


	* TEMA 38


	* Como trabajar con un Puntero de texto.

		-> En el siguiente código, nos imprimiria el texto guardado de principio a fin. El puntero inicialmente
		se encontraría en el inicio del texto y tras su impresión quedaría al final, de modo que si tuvieramos
		que volver a imprimir ese texto no se produciría, ya que el puntero se encuentra al final.
		Para ello necesitamos colocar el puntero en la posición que necesitemos, y lo haríamos con el metodo "seek()",
		que lo usamos para colocarlo en la posición del nº de letras indicado.
'''

	from io import open

		archivo_texto = open("archivo.txt", "r")

		print(archivo_texto.read())
		print(archivo_texto.read())

		print(archivo_texto.seek(0))

		print(archivo_texto.read(11))

	#-> Con el siguente ejemplo conseguimos manipular el puntero para colocarlo en la mitad del texto.

	from io import open

		archivo_texto = open("archivo.txt", "r")

		archivo_texto.seek(len(archivo_texto.read())/2)

		print(archivo_texto.read())

	#-> Si usamos el metodo "readlines()" leeriamos y colocarimos el puntero de linea en linea.

	archivo_texto.seek(len(archivo_texto.readlines()))

	#-> Podemos tambien combinar metodos para convertir el "open" en archivo de escritura y lectura.

	archivo_texto = open("archivo.txt", "r+") # añadiendo el "+"

	archivo_texto.write("Comienzo del texto") #