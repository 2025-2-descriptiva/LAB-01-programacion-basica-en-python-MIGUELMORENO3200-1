"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    x = open("files/input/data.csv", "r").readlines() # Abrir archivo y leer todas las líneas
    x = [z.replace("\n", "") for z in x] # Quitar saltos de línea al final
    x = [",".join(z.strip().split("\t")) for z in x] # Reemplazar tabuladores por comas usando join y split
    x = [z.split(",") for z in x]

    total = 0
    for row in x:
        total+=int(row[1])
    
    return total
