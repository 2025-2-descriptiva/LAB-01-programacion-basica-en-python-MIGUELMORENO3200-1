"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    x = open("files/input/data.csv", "r").readlines()  # Abrir archivo y leer todas las líneas
    x = [z.replace("\n", "") for z in x]  # Quitar saltos de línea al final
    x = [",".join(z.strip().split("\t")) for z in x]  # Reemplazar tabuladores por comas
    x = [z.split(",") for z in x]

    max_min_por_letra = {}
    for z in x:
        x_letra = z[0]
        x_numero = int(z[1])
        if x_letra not in max_min_por_letra:
            max_min_por_letra[x_letra] = (x_numero, x_numero)
        else:
            max_actual, min_actual = max_min_por_letra[x_letra]
            max_min_por_letra[x_letra] = (max(max_actual, x_numero), min(min_actual, x_numero))

    resultado = [(letra, max_min_por_letra[letra][0], max_min_por_letra[letra][1]) for letra in sorted(max_min_por_letra.keys())]
    return resultado



