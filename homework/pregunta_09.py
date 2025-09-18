"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    x = open("files/input/data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [",".join(z.strip().split("\t")) for z in x]
    x = [z.split(",") for z in x]

    conteo = {}

    for fila in x:
        for col in fila[5:]:  # desde la columna 6 en adelante
            if ":" in col:
                clave, _ = col.split(":")
                if clave not in conteo:
                    conteo[clave] = 1
                else:
                    conteo[clave] += 1

    resultado = dict(sorted(conteo.items()))
    return resultado
pregunta_09()