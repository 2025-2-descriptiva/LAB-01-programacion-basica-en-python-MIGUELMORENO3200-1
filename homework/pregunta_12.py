"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de todos los valores desde la columna 5 en adelante.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    x = open("files/input/data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [",".join(z.strip().split("\t")) for z in x]
    x = [z.split(",") for z in x]

    suma_columna_5 = {}

    for fila in x:
        letra = fila[0]
        total = 0
        # Recorrer todas las columnas desde la 5 en adelante
        for col in fila[5:]:
            if ":" in col:
                _, valor = col.split(":")
                total += int(valor)
        # Acumular la suma por la letra de la columna 1
        if letra in suma_columna_5:
            suma_columna_5[letra] += total
        else:
            suma_columna_5[letra] = total

    return dict(sorted(suma_columna_5.items()))

print(pregunta_12())


