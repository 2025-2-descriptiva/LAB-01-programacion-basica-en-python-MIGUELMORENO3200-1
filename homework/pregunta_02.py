"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    from collections import Counter
    x = open("files/input/data.csv", "r").readlines() # Abrir archivo y leer todas las líneas
    x = [z.replace("\n", "") for z in x] # Quitar saltos de línea al final
    x = [",".join(z.strip().split("\t")) for z in x] # Reemplazar tabuladores por comas usando join y split
    x = [z.split(",") for z in x]
    list_c = [z[0] for z in x]

    return sorted(Counter(list_c).items())

print(pregunta_02())




    
