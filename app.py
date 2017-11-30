"""Proyecto Prediccion de Elecciones."""
import numpy as np
import funciones.Values as v
import funciones.apriori as ap
from funciones.Mxlsx import ReadLog

# info del log
# 2 distrito
# 3 puesto
# 4 - 18 partidos
# 19 hombres , 20 mujeres
# 21 activo , 22 no activo (economia)
# 23 grado de escolaridad
# 24 con, 25 sin (religion)


def normalizeData(data):
    """Normalizar datos para clasificar etiquetas."""
    # agregar distrito y puesto tal cual
    aDataNorm = data[:, 2:4]
    # asignar el ganador de las Elecciones
    listPartidoKey = np.argmax(data[:, 4:18], axis=1)
    listpartido = v.getPartido(listPartidoKey)
    aDataNorm = np.concatenate((aDataNorm, listpartido), axis=1)
    # asignar genero
    listGeneroKey = np.argmax(data[:, 19:21], axis=1)
    listGenero = v.getGenero(listGeneroKey)
    aDataNorm = np.concatenate((aDataNorm, listGenero), axis=1)
    # asignar rangos valores numemerica
    aDataNorm = np.concatenate((aDataNorm, data[:, 21:26]), axis=1)
    return aDataNorm


ListP = ["nan", "nan", "nan", "nan", 50000, 50000, 4, 100000, 12000]
L = ReadLog("doc/logElecciones.xlsx")
data = np.array(L.filas)
data = normalizeData(data)
# nombre de cada columna solo agregar al final
head = ["", "distrito",
        "puesto", "partido", "genero", "economia activa",
        "economia inactiva", "grado de escolaridad", "con religion",
        "sin religion"]
ap.setData(data, ListP)
ap.classifyItems(head)
# obtener las reglas primer parametro es el soporte segundo es Confianza
ap.getRule()
