# CONDICIONALES 
	#TEMA 10

	# La Instruccion IF

		# SINTAXIS:  if condicional:


print("Programa de evaluacion de notas de alumnos")

nota_alumno=input("Introduce nota:")

def evaluacion(nota):
	valoracion="aprobado"

	if nota<5:
		valoracion="suspenso"

	return valoracion

print(evaluacion(int(nota_alumno)))


#CONDICIONALES II
	#TEMA 11

	# Instruccion IF acompañada por intrucciones:
		# ELSE(y si no es verdad ) y 
		# ELIF(Condiconales intermedios)


print("Verificación de acceso")

edad_usuario=int(input("Introduce tu edad, por favor:"))

if edad_usuario<18:				# La condicion se cumple si es verdadera.
	print("No puedes pasar.")

elif edad_usuario>100			# La condicion se cumple si es verdadera y el if no.
	print("Edad incorrecta")

else:							# Si ninguna es verdadera se ejecutara el else.
	print("Puedes pasar.")

print("El programa ha finalizado")



# CONDICIONALES III
	# TEMA 12

	# Concatenacion de operadores de comparación.
		

edad=7

if 0-edad<100:					# Si la 1ª condicion(0) es falsa se salta el "if" si es cierta continua 
	print("Edad es correcta")	# evaluando la edad(<100)
else:
	print("Edad es incorrecta")


salario_presidente=int(input("Introduce salario Presidente:"))
print("Salario Presidente:" + str(salario_presidente))

salario_director=int(input("Introduce salario Director:"))
print("Salario Director:" + str(salario_director))

salario_jefe_area=int(input("Introduce salario Jefe de Area:"))
print("Salario Jefe de Area:" + str(salario_jefe_area))

salario_administrativo=int(input("Introduce salario del Administrativo:"))
print("Salario del Administrativo:" + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente: #Concatenacion de condicionales.
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")



# CONDICIONALES IV
	# TEMA 13
		# Operadores logicos "and"(y si tambien) y "or"(o si no)
		# Operador "in"()

print("Programa de Becas 2022")

distancia_escuela=int(input("Introduce la distancia a la escuela en km:"))
print(distancia_escuela)

numero_hermanos=int(input("Indica el numero de hermanos:"))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto:"))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000: #Uso del condicional "and" y concatenado.

	print("Tienes derecho a Beca.")
else:
	print("No tienes derecho a Beca.")


if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000: # Uso del condicional "or", modificando el "if" anterior.

# Uso del condcional "in".

print("Asignaturas optativas Año 2022")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

asignatura=input("Escribe la asignatura escogida: ")

# Cambio de comando para trasformar la respuesta en minuscula y no da errores por es cribir en minuscula o mayuscula.
		# .lower() para hacerlas toda minusculas.
		# .upper() para transformarlas en mayuscalas.

#	1- opcion==input("Escribe la asignatura escogida: ")
#	2- asignatura=opcion.lower()  

if asignatura in ("Informatica grafica", "Pruebas de software", "Usabilidad y accesibilidad"):

	#if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
	# esta linea escribiriamos todos lo parametros en minuscula.

	print("Asignatura elegida" + asignatura)

else:
	print("La Asignatura elegida no esta contemplada.")

