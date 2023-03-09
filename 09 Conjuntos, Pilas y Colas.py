	#	LOS CONJUNTOS

# Son una coleccion donde los elementos se agregan de forma desordenada.
# Su principal caracteristica es que no PUDE HABER DUPLICADOS. Ni tampoco
# otra colencion dentro de los conjuntos.
# En ellos podremos buscar con la condicion "in", al igual que en otros.

	# SINTAXIS: conjunto = set()  -> Se creara un conjunto vacio para añadir
			# posteriormente elementos.
	# SINTAXIS:VPara la creacion de un conjunto: (elementos separados por ",")
				conjunto = {}

conjunto = set()
conjunto = {1,2,3,"Hola,",3.45}
print(conjunto)

	# Para agregar mas elementos al conjunto se usa ".add"
	# Se añadiran de forma desordenada en su interior.
	conjunto.add(5,6)

	# Si queremos eliminar un elemento usaremos ".discard".
	conjunto.discard(3)

	# Para eliminar todo el conjunto utilizaremos ".clear"
	conjunto.clear()


	# OPERACIONES con CONJUNTOS

a = {1,2,3}
b = {4,5,6}

	# Para hacer la igualdad de 2 Conjuntos:
	print(a == b)	# Estamos preguntando si hay igualdad en los conjuntos y nos dar "True" o "False".
					# No importara el orden de los elementos para su igualdad.

	# Metodo "len" para saber el nº de elementos.
	print(len(a))

	# LA UNION
	# Nos mostrara los elementos que existe en ambos conjuntos. (c=a+b nos daria un error)
	# Y los elementos repetidos se mostraran solo una vez.
	c = a | b
	print(c)

	# LA INTERCEPCION
	# Nos muestra los elementos que estan en ambos conjuntos.
	c = a & b
	print(c)

	# LA DIFERENCIA
	# Nos muestra los elementos que estarian en "a" y no en "b", o viceversa.
	c = a - b
	# o
	c = b - a 
	print(c)

	# LA DIFERENCIA SIMETRICA
	# Nos muestra los elementos que estan en "a" y en "b", pero no en ambos.
	c = a ^ b
	print(c)

	# Podemos conocer si un Conjunto esta dentro de Otro, con ".issubset" :
	c = {1,2,3,4,5,6}
	print(a.issubset(c))	# Nos daria "True", pues "1,2,3" estan dentro de "c"
							# Siempre que esten todos los elementos.

	# EL SUPER CONJUNTO
	# Conoceriamos de igualforma si todos los elementos de "a" o "b" estan en "c". (True o False)
	print(c.issuperset(b))

	# Si queremos saber si los conjuntos son DISCONECSOS, si no tienen ningun elmento en comun. _(True o False)
	print(a.isdisjoint(b))

	# Para haccer un Conjunto INMUTABLE(no modificable), usariamos "frozenset()"
	a = frozenset({7,8,9})
	

