"""Valores Iniciales del Codigo."""
import numpy as np

Listpartido = ["PAN",
               "PRI",
               "PRD",
               "VERDE",
               "PT",
               "MOV. CIU.",
               "NUEVA ALIANZA",
               "MORENA",
               "HUMANISTA",
               "ENC. SOC",
               "INDEP.	ALTERNATIVA",
               "No registrados",
               "Votos nulos"]
ListGenero = ["Hombre",
              "Mujer"]


def getPartido(listPartidoKey):
    """Obtener el nombre de los partidos."""
    winPartido = []
    for i in range(len(listPartidoKey)):
        winPartido.append([Listpartido[listPartidoKey[i]]])
    return np.array(winPartido)


def getGenero(listGeneroKey):
    """Obtener el genero que predomina."""
    prGenero = []
    for i in range(len(listGeneroKey)):
        prGenero.append([ListGenero[listGeneroKey[i]]])
    return np.array(prGenero)

# a = np.arange(16).reshape((4, 4))
#
# print(a)
# print("--")
# print(np.amax(a, axis=1))
# print("--")
# print(np.argmax(a, axis=1))
