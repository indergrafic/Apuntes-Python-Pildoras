"""
	TEMA 55

	---- BASE DE DATOS - BBDD------

	--> Creación de BBDD
		- Conexión con BBDD
		- Inserción de registros en BBDD


	Python puede manegar diferentes Sistemas Gestores de Base de Datos (SGDB)
	SQL -> (Structured Query Language) Lenguage de Acceso a datos Estructurado.

	 - SQL Server
	 - Oracle
	 - MySql
	 - SQLite
	 - PostgreSQL
	 - Etc..

	----------------
	¿Qué es SQLite?

		- Sistema de gestión de BBDD relacional.
		- Escrito en C, es de codigo abierto.
		- Forma parte integral del programa.
		- Se guarda como un único fichero en host.

		VENTAJAS												INCONVENIENTES

	- Ocupa muy poco espacio de disco y memoria				- No admite clausulas anidadas (where)
	- Muy eficiente y rápido								- No existen usuarios (no acceso simultáneo por parte de varios a la vez)
	- Multiplataforma										- Falta de clave foránea duando se crea en modo consola
	- Sin administración / configuración
	- Dominio público. Sin costo.

	--> Pasos a seguir para conectar con una BBDD

		1. Abrir-Crear conexión
		2. Crear puntero (o cursor)
		3. Ejecutar query (consulta) SQL
		4. Manejar los resultados de la query (consulta)
			1. Insertar, Leer, Actualizar, Borrar (Create, Read, Update, Delete)
		5. Cerrar puntero
		6. Cerrar conexión

"""


import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

# En la linea comentada: Creamos la base de datos y sus parametros. (Solo podemos hacerlo una vez, sino nos dara error)
# --> miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCTION VARCHAR(20))")

# Introducimos datos dentro de la tabla creada de la BBDD
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

# Cada vez que hacemos un cambio en BBDD o añadimos datos hay que hacer un "commit"
miConexion.commit()




miConexion.close()



'''
	TEMA 56

	-> Inserción de varios registro (insertar a la vez varios registros)

	-> Recuperación de varios registros (leer la infomarción del registro)


'''


import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

# Insertando varios productos en la BBDD
variosProductos=[
	
	("Camiseta", 10, "Deportes"),
	("Jarron", 90, "Ceramica"),
	("Camion", 10, "Jugueteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)


# ---> Recuperar la información de la BBDD

miCursor.execute("SELECT * FROM PRODUCTOS") # Si añadimos a continuación de PRODUCTOS ->"WHERE SECCION='Deportes'
											# estamos solicitando todos los aticulos de esa sección 
variosProductos = miCursor.fetchall()

print(variosProductos)


# Cada vez que hacemos un cambio en BBDD o añadimos datos hay que hacer un "commit"
miConexion.commit()


miConexion.close()




'''
	TEMA 57

	-> Gestionar la Claves pricipales de las BBDD
		Cada registro debe estar identificado por un Campo Clave
		como si se tratase de un dni que lo individualiza de los demás.

	
'''

import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

#	Si cambiamos la linea escrita por la comentada el codigo articulos e incrementara de forma automática.
miCursor.execute('''
	CREATE TABLE PRODUCTOS (
	CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY, -->  (ID INTEGER PRIMARY KEY AUTOINCREMENT,)
	NOMBRE_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos = [

	("AR01", "pelota", 20, "jugueteria"),
	("AR02", "pantalon", 15, "confeccion"),
	("AR03", "matillo", 25, "ferreteria"),
	("AR04", "jarron", 45, "ceramica")
]

#--> Tamién para hacerlo automatico debemos cambiar a (NULL,?,?,?), para que no de error, ya que le pasamos un argumento menos.
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

miConexion.commit()


miConexion.close()


'''
	TEMA 58

	-> Cláusula UNIQUE (impedira poder repetier un campo en la BBDD)

	-> Operaciones CRUD (significa- Cread(crate), Leer(read), actualizar(update) y borrar(delete))

	
'''

import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()


miCursor.execute('''
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE, #PARA QUE NO SE PUEDA REPETIR EL NOMBRE DEL ARTICULO
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

# SI QUEREMOS ACTUALIZAR UN CAMPO CAMBIANDO SU VALOR HABRIA QUE HACERLO ASÍ: en este caso el precio de la pelota.
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")


# SI LO QUE QUEREMOS HACER ES BORRAR UN PRODUCTO O UN CAMPO: (cuidado por que si hay dos campos iguales se borrarian todos)
miCursor.execute("DELETE PRODUCTOS SET PRECIO=35 WHERE ID=5")



productos = [

	("AR01", "pelota", 20, "jugueteria"),
	("AR02", "pantalon", 15, "confeccion"),
	("AR03", "matillo", 25, "ferreteria"),
	("AR04", "jarron", 45, "ceramica")
]

#--> Tamién para hacerlo automatico debemos cambiar a (NULL,?,?,?), para que no de error, ya que le pasamos un argumento menos.
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

miConexion.commit()


miConexion.close()