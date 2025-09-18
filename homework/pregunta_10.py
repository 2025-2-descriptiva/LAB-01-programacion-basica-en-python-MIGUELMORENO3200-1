"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla,
    la letra de la columna 1 y la cantidad de elementos de las columnas 4 y 5.
    """
    x = open("files/input/data.csv", "r").readlines()
    x = [z.strip().split("\t") for z in x]  # usar tabulador directamente

    resultado = []
    for fila in x:
        letra = fila[0]
        col4 = fila[3].split(",") if fila[3] else []
        col5 = fila[4].split(",") if fila[4] else []
        resultado.append((letra, len(col4), len(col5)))

    return resultado
print(pregunta_10())