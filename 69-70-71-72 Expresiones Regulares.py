'''
    TEMA 69

    -------EXPRESIONS REGULARES------------

    ¿Qué son?

    -> Las expresiones regulares son  una secuancia de caracteres que forman un 
    patron de busqueda.

    ¿Para qué sirver?

    -> Para el trabajo y procesamiento de texto.

    Ejemplos:

    * Buscar un texto que se ajusta a un formato determinado (correo electronico).
    * Buscar si existe o no una cadena de caracteres dentro de un texto.
    * Contar el número de coincidencias dentro de un texto.
    * Etc...
'''

import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de progamación sencilla"

print(re.search("aprender", cadena)) # Metodo search

# Ejemplo con start (inprime la posición inicial de la palabra buscada)
cadena = "Vamos a aprender expresiones regulares"

textoBuscar = "aprender"

textoEncontrado = re.search(textoBuscar, cadena)

print(textoEncontrado.start()) # imprimirá (8)

print(textoEncontrado.end()) # imprimirá el nº del ultimo caractrer (16)

print(textoEncontrado.span()) # imprimirá inicio y final en una tupla (8, 16)

textoBuscar = "Python"

print(re.findall(textoBuscar, cadena)) # nos devuelve un a lista con las veces encontradas = [Python, Python]



'''
    TEMA 70

    ------Los Metacaracteres (caracteres comodín)-------

    -> Anclas y clases de caracteres
'''

import re

lista_nombres = ['Ana Gómez'
                 'Maria Martin'
                 'Sandra López'
                 'Santiago Martín'
                 'Sandra Hernandez']

for elemento in lista_nombres: # '^' nos busca nombres que empiezan por la palabra a indicada
    if re.findall('^Sandra', elemento):
        print(elemento)

for elemento in lista_nombres: # '$' nos busca nombres que terminan por la palabra a indicada
    if re.findall('Martín$', elemento):
        print(elemento)

    if re.findall('[Gó]', elemento): # Buscaria las coincidencias del o los caractes indicados
        print(elemento)             # aunque no estesn en ese orden. (Ana Gomez) es  lo que devolveria.

# En el sigueinte ejemplo buscamos nombres o palabras acentudada y sin acentuar.
if re.findall('Mart[ií]n', elemento):
        print(elemento)


'''
    TMEA 71

    ------------Rangos-----------------

        -> Busqueda de elementos dentro de una lista un rango de caracteres, numeros, mezcla etc.
'''

lista_nombres = ['Ana'
                 'Pedro'
                 'Maria'
                 'Rosa'
                 'Sandra'
                 'Celia']

for elemento in lista_nombres: # nos busca nombres que esten dentro del rango de la 'o' y la 't'
    if re.findall('[o-t]', elemento): # diferencia entre mayusculas y minusculas, dando otro resultado.
        print(elemento)               # y se pueden añadir elementos anteriores.


'''
    TENA 72

    ------Funciones del modulo re ----------------------

    -> Match y search

    Match busca y hay coincidencias al comienzo de una cadena de texto.
    Search busca en toda la cadena de texto si encuentra el patron de busqueda.
'''

import re

nombre1 = 'Sandra López'
nombre2 = 'Antonio Gómez'
nombre3 = 'María López'
nombre4 = 'sandra Pérez'

# usando "re.IGNORECASE" nos ignora en la busqueda las mayuslas y minusculas.
if re.match('Sandra', nombre1, re.IGNORECASE):
     print('Hemos encontrado el nombre')
else:
     print('no lo hemos encontrado')

# Busqueda con "Search"
nombre1 = 'Sandra López'
nombre2 = 'Antonio Gómez'
nombre3 = 'María López'
nombre4 = 'sandra Pérez'

# usando "re.IGNORECASE" nos ignora en la busqueda las mayuslas y minusculas.
if re.search('López', nombre1):
     print('Hemos encontrado el nombre')
else:
     print('no lo hemos encontrado')