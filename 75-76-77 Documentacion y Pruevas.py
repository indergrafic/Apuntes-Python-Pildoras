'''
    TEMA 75

    ---------Documentar un Programa-------------

    ¿Qué es?
    -> Incluir comentarios en clases, métodos, módulos, etc.

    ¿Para qué?
    -> Para ayudar en el trabajo en equipo. Especialmente útil en aplicaciones complejas.
'''

def areaCuadrado(lado):
    """ Calcula el área de un cuadrado elevado
    al cuadrado el lado pasado por parametro"""

    return "El área del cuadrado es: " + str(lado*lado)

print(areaCuadrado(3))

print(areaCuadrado.__doc__) # Nos va a imprimir las notas dentro de la funcion que hallamos escrito

help(areaCuadrado) # En este caso no necesitamos indicar que la imprima

class Calculo:
    """Clase para crear funciones de calculo"""

    def areaCuadrado(lado):
        """ Calcula el área de un cuadrado elevado
        al cuadrado el lado pasado por parametro"""

        return "El área del cuadrado es: " + str(lado*lado)
    
help(Calculo.areaCuadrado) # En el caso de las Clases debemos indicar la clase y la función para acceder a la información

help(Calculo) # Nos informara de toda la información dentro de esa clase.

'''Si tenemos un modulo independiente y lo llamamos tambien podemos acceder con "help" a su información
Este sería un ejemplo si existiese un modulo llamado funciones_matematicas'''

from modulos import funciones_matematicas

help(funciones_matematicas)


'''
    TEMA 76

    -----------Utilizar la Documentación para realizar Pruebas------------

        * Modulo doctest (trabajaremos con él y habra que importarlo)
        
        -> El sentido de ello es hacer pruebas de lo programado para saber si lo que estamos programando va funcionando.
            De modo que si creamos una funció por ejemplo, podemos probar si esta funcina corectamente antes de seguir con ella.

        1º - Documentaremos la función.
        2º - Hay que (normalmente) colocar debajo de la Documentación y dentro de las comillas,
            3 mayor que ">>>" el nombre de la función y en los paréntesis datos de los argumentos pedidos.
            Y debajo aquel resultado que deba dar dicha función. Ese resultado debe ser exactamente
            lo esperado, enteros, cadena de caracteres, etc.. En caso contrario fallara.
        3º - Bajo la función se escribe el modulo a importar y el metodo para hacer la prueba.
        4º - Si test funciona, no nos devolvera nada, en caso contrario nos dara un mensaje de fallo,
            en el que no indicara donde y el resultado dado y el que debería dar en caso de funcionar.
'''



def areaTriangulo(base, altura):

    """ 
    Calcula el area de un Triangulo dado
    
    >>> areaTriangulo(3, 6)
    9.0
    """

    return (base*altura)/2

import doctest
doctest.testmod()


# En este ejemplo hemos añadido un str, debiendo devolver lo esperado si no hemos cometido error.
def areaTriangulo(base, altura):

    """ 
    Calcula el area de un Triangulo dado
    
    >>> areaTriangulo(3, 6)
    'El area del Triangulo es: 9.0'
    """

    return "El area del Triangulo es: " + str((base*altura)/2)

import doctest
doctest.testmod()


# Podemo o si necesitamos hacer varias pruebas, concatenar varias pruebas en la misma función.
def areaTriangulo(base, altura):

    """ 
    Calcula el area de un Triangulo dado
    
    >>> areaTriangulo(3, 6)
    'El area del Triangulo es: 9.0'

    >>> areaTriangulo(4, 5)
    'El area del Triangulo es: 10.0'
    """

    return "El area del Triangulo es: " + str((base*altura)/2)

import doctest
doctest.testmod()

''' A continuación un ejmeplo mas elaborado para examinar si la función hace lo que esperamos o es erronea'''

def compruebaMail(mailUsuario):

    '''
    La función compruebaMail evalúa un mail recibido en busca
    de la @. Si tiene una @ es correcto, si tiene más de una @
    es incorrecto y si la @ esta al final es icorrecto.

    >>> compruebaMail('juan@cursos.es')
    True

    >>> compruebaMail('juancursos.es@')
    False

    >>> compruebaMail('juancursos.es')
    False

    >>>compruebaMail('juan@curso@s.es')
    False

    '''

    arroba = mailUsuario.count('@')

    if (arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
        return False
    else:
        return True
    
import doctest
doctest.testmod()



'''
    TEMA 77

    ------------Utilizar la documentación para realizar pruebas-------------

    *   Usaremos el modulo "doctest" pero para realzar prubas mas complejas.
        Se usara pruebas con elementos anidados usando "..." para indicarlo como si estubiera identado.
'''

import math

def raizCuadarada(listaNumeros):

    '''
    La función devuelve una lista con la raíz cuadarada de los
    elementos numéricos pasados por parámetros en otra lista.

    >>> lista=[]
    >>> for i in [4, 9 , 16]:
    ...   lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista=[]
    >>> for i in [4, -9 , 16]:
    ...   lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last).
        ...
    ValueError: math domain error
    '''
    # En la prueba de arriba los tres "..." son usado en sustitucion del las lineas de mensage que proporcionará
    # el error. La prueba saldara correcta porque test es correcto con lo esperado al indicar un número (-9) negativo.
    # Si no hubiera un número negativo el test no pasará
    return [math.sqrt(n) for n in listaNumeros]

import doctest
doctest.testmod()