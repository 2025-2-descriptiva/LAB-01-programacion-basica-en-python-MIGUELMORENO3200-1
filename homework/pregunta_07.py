"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    x = open("files/input/data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [",".join(z.strip().split("\t")) for z in x]
    x = [z.split(",") for z in x]

    letras_por_numero = {}
    for fila in x:
        letra = fila[0]
        numero = int(fila[1])
        if numero not in letras_por_numero:
            letras_por_numero[numero] = [letra]
        else:
            letras_por_numero[numero].append(letra)

    resultado = [(numero,(letras_por_numero[numero])) for numero in sorted(letras_por_numero.keys())]
    return resultado

print(pregunta_07())
