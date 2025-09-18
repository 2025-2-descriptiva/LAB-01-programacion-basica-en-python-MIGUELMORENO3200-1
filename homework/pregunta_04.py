"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
    """
    x = open("files/input/data.csv", "r").readlines()  # Abrir archivo y leer todas las líneas
    x = [z.replace("\n", "") for z in x]  # Quitar saltos de línea al final
    x = [",".join(z.strip().split("\t")) for z in x]  # Reemplazar tabuladores por comas
    x = [z.split(",") for z in x]

    registros_por_mes = {}
    for z in x:
        fecha = z[2]
        mes = fecha.split("-")[1]
        if mes in registros_por_mes:
            registros_por_mes[mes] += 1
        else:
            registros_por_mes[mes] = 1

    return sorted(registros_por_mes.items())
