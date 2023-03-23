'''
    TEMA 73

    ---------FUNCIONES DECORADORES-------------
    
    -> Qué son, como funcionan y Sintaxis.

    * Son funciones que a su vez añaden funcionalidades a otras funciones.
        - Por eso se las denomina "decoradores", porque "decoran" a otras funiones.
        Les añaden funcionalidades.

    * Estructura de un decorador:
        - 3 funciones (A, B, y C) donde A recibe como parametro a B para devolver C.
        - Un decorador devuelve una función.

    * Su extructura o Sintaxis:

            def funcion_decorador(funcion):
                def funcion_interna():
                    # código de la función interna
                return función_interna

    Ejemplo:
'''
def funcion_decoradora(funcion_parametro):

    def funcion_interior():

        # Acciones adicionales que decoran

        print("vamos a realizar un cálculo")

        funcion_parametro()

        # Aciones adicionales que decoran

        print("Hemos terminado el cálculo")

    return funcion_interior

@funcion_decoradora # Añadiendo esta nomenclatura estamos indicando que la siguiente funcion será decorada con la funcion decoradora.
def suma():
    print(15+20)

def resta(): # Para decorar esta u otras habrá que hacer lo mismo que con la anterior.
    print(30-10)

suma()
resta()

'''
    TEMA 74
    
    -----------CREAR DECORADORES CON PARAMETROS----------------

    uso de la nomemclatura en los paramentros de " *args "  y  " **kwargs "

'''

def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args,         # nomenclatura para recivier cualquier numero de parametros
                          **kwargs):        # en este caso se pasan argumentos con "clave-valor"

        # Acciones adicionales que decoran

        print("vamos a realizar un cálculo")

        funcion_parametro(*args, **kwargs) # Aqui tambien habria que colocar el "**Kargs"

        # Aciones adicionales que decoran

        print("Hemos terminado el cálculo")

    return funcion_interior

@funcion_decoradora # Añadiendo esta nomenclatura estamos indicando que la siguiente funcion será decorada con la funcion decoradora.
def suma(num1, num2):
    print(num1+num2)

@funcion_decoradora
def resta(num1, num2): # Para decorar esta u otras habrá que hacer lo mismo que con la anterior.
    print(num1-num2)
    
@funcion_decoradora
def potencia(base, exponente):
    print(base, exponente)

suma(7, 5)
resta(12, 10)
potencia(base=5, exponente=3) # es en este caso cuando usamos "**Kwargs"(base es la clave y 5 el valor-- y -- exponenete es la clave y 3 el valor)