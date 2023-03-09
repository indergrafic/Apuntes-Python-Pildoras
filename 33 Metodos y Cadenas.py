'''
	METODOS Y CADENAS

	---- TEMA 33 ----

	* Uso de métodos de cadenas (String) 

	upper()			lower()			capitalize()		count()

	find()			isdigit()		isalum()			isalpha()

	split()			strip()			replace()			rfind()

	'''

	nombreUsuario = input('Introduce tu nombre de Usuario')

	print('El nombre es: ', nombreUsuario.upper()) # Canbia el nobre a Mayuscualas
	print('El nombre es: ', nombreUsuario.capilatice()) # Cambia la primera letra a mayuscula

	edad = input('Introduce la edad: ')

	print(edad.isdigit()) # Nos devuelve True o False si se introduce un digito o una cadena

	# Ejm. sencillo donde usamo la funcion para comprovar que introducimos un numero
	while (edad.isdigit()==False:
		print('Por favor, introuduce un valor numerico')
		edad = input('Introduce la edad: ')
		
	if (int(edad)<18):
		print('No puede pasar')
	else:
		print('Puedes pasar')