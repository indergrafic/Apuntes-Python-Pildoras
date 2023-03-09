"""
    TEMA 66

    ----Funciones Lambda-------

    -> ¿Qué son y cuál es su utilidad?

    Su utilidad es para hacer que una funcion normal sea mas ligera y abreviar, ahorrando tiempo.

    Si la funcion que queremos resumir es compleja no podremos hacerlo con la función "lambda"
    no podra tener bucles o condicionales.
"""
# Funcion Tradicional
def area_triangulo(base, altura):

    return (base * altura) / 2

# Fundion resumida con la función "lambda". Los : corresponden al return de la tradicional.
area_triangulo = lambda base, altura:(base * altura)/ 2


"""
    TEMA 67

    ----Funciones Filter-----

    -> ¿Qué son y su Utilidad?

    Son funciones de las denominadas de nivel superior. Y nos van a facilitar hacer uso de un paradigma
    que se denomina "Programación Funcional".

    Lo que hace es: verifica que los elementos de una secuencia cumplen una condición, devolviendo un
    iterador con los elementos que cumple dicha condición.
"""
# Funcion para que nos diga que numeros son pares y cules no.

def numero_par(num):

    if num % 2==0:
        return True
    
numeros=[17,24,7,39,8,51,92]

# Usando la funcion "Filter" para imprimir una lista con los numeros pares
print(list(filter(numero_par, numeros)))

# Mezclando el uso de esta función con la anterior "Lambda"

print(list(filter(lambda numero_par: numero_par%2==0, numeros)))


class Empleado:

    def __init__(self, nombre, cargo, salario):
        
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)
    
listaEmpleado = [
Empleado("Juan", "Director", 75000),
Empleado("Pedro", "Secretaria", 45000),
Empleado("Ana", "Botones", 33000),
Empleado("Andres", "Administrativo", 55000),
]

salarios_altos = filter(lambda empleado:empleado.salario>35000, listaEmpleado)

for emplado_salario in salarios_altos:
    print(emplado_salario)



    """
    TEMA 68

    ----Funciones Map-----

    -> ¿Qué son y su Utilidad?

    Aplica una función a cada elemento de una lista iterable (listas, tuplas, etc..)
    devolviendo una lista con los resultados.
"""


class Empleado:

    def __init__(self, nombre, cargo, salario):
        
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)
    
listaEmpleado = [
Empleado("Juan", "Director", 7500),
Empleado("Pedro", "Secretaria", 4500),
Empleado("Ana", "Botones", 3300),
Empleado("Andres", "Administrativo", 5500),
]

def calculo_comision(empleado):

    empleado.salario = empleado.salario*1.03

    return empleado

listaEmpleadosComision = map(calculo_comision, listaEmpleado)

for empleado in listaEmpleadosComision:

    print(empleado)