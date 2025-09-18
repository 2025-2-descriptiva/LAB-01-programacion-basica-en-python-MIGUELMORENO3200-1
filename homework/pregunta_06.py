def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]
    """
    x = open("files/input/data.csv", "r").readlines()
    x = [z.replace("\n", "") for z in x]
    x = [",".join(z.strip().split("\t")) for z in x]
    x = [z.split(",") for z in x]

    max_min_por_codigo = {}

    for fila in x:
        for col in fila[5:]:  # desde la columna 6 en adelante
            if ":" in col:
                clave, valor = col.split(":")
                valor = int(valor)
                if clave not in max_min_por_codigo:
                    max_min_por_codigo[clave] = (valor, valor)
                else:
                    min_actual, max_actual = max_min_por_codigo[clave]
                    max_min_por_codigo[clave] = (min(min_actual, valor),
                                                 max(max_actual, valor))

    resultado = [(clave, v[0], v[1]) for clave, v in sorted(max_min_por_codigo.items())]
    return resultado

