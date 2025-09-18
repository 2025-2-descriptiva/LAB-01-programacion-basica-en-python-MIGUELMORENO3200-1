"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra individual que aparece antes de los datos con ':', ordenadas alfabeticamente.
    """
    suma_por_letra = {}

    with open("files/input/data.csv", "r") as f:
        for linea in f:
            fila = linea.strip().split("\t")
            if fila[0] == "col1":  # saltar encabezado
                continue
            numero = int(fila[1])
            
            # Procesar letras individuales
            for item in fila[3:]:
                if ":" in item:  # parar cuando llegamos a datos con ":"
                    break
                # separar si hay varias letras juntas con coma
                letras = item.split(",")
                for letra in letras:
                    letra = letra.strip()
                    if letra in suma_por_letra:
                        suma_por_letra[letra] += numero
                    else:
                        suma_por_letra[letra] = numero

    return dict(sorted(suma_por_letra.items()))

print(pregunta_11())




