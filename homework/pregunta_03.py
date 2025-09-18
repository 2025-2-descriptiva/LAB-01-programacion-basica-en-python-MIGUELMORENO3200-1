"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordenadas alfabéticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
    """
    x = open("files/input/data.csv", "r").readlines()  # Abrir archivo y leer todas las líneas
    x = [z.replace("\n", "") for z in x]  # Quitar saltos de línea al final
    x = [",".join(z.strip().split("\t")) for z in x]  # Reemplazar tabuladores por comas
    x = [z.split(",") for z in x]

    suma_por_letra = {}
    for z in x:
        letra = z[0]
        valor = int(z[1])
        if letra in suma_por_letra:
            suma_por_letra[letra] += valor
        else:
            suma_por_letra[letra] = valor

    return sorted(suma_por_letra.items())

print(pregunta_03())

