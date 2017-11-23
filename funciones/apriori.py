"""Clase Apriori."""
import numpy as np
from apyori import apriori

label = []
listLabel = []
Listcategoric = []


def setData(data, ListParameter=0):
    """Asignar data para Apriori."""
    global label, ListP
    label = data.copy()
    ListP = ListParameter


def rangeNumeric(c, v):
    """Clasificar Numerica."""
    keylist = list()
    lmin = int(min(label[:, c]))
    lmax = int(max(label[:, c]))
    lenR = ListP[c]
    key = 0
    limu = 0
    print("min: ", lmin, " max: ", lmax)
    for limB in range(lmin + lenR, lmax + 1, lenR):
        limA = limB - lenR
        limA = limA + 1 if limA != lmin else limA
        r = label[:, c]
        for x in range(len(r)):
            if type(r[x]) == str:
                r[x] = int(r[x])
        clave = str(c) + str(key)
        label[:, c][(r >= limA) & (r <= limB)] = clave
        key += 1
        limu = limB
        keylist.append(v + "[" + str(limA) + "-" + str(limB) + "]")
        print(" [", limA, "-", limB, "]")
    if limu != lmax:
        r = label[:, c]
        for x in range(len(r)):
            if type(r[x]) == str:
                r[x] = int(r[x])
        clave = str(c) + str(key)
        label[:, c][(r >= limu) & (r <= lmax)] = clave
        keylist.append(v + "[" + str(limu) + "-" + str(lmax) + "]")
        print(" [", limu, "-", lmax, "]")
    listLabel.append(keylist)


def rangeCategoric(c, v):
    """Clasificar Catgorica."""
    keylist = list()
    columna = label[:, c]
    listcategoric = np.unique(columna)
    for i, categoric in enumerate(listcategoric):
        columna[columna == categoric] = str(c) + str(i)
        keylist.append(v + "[" + categoric + "]")
    label[:, c] = columna
    listLabel.append(keylist)


def showLabel(tlabel):
    """Mostrar el valor de item."""
    cadena = ""
    for co in tlabel:
        coc = int(co[0])
        cof = int(co[1])
        cadena += " | " + listLabel[coc][cof]
    # print(cadena)
    return cadena


def classifyItems(head):
    """Clasificacion items."""
    # clasificar etiquetas
    for i, variable in enumerate(head):
        if i == 0:
            continue
        print("variable: ", variable)
        try:
            int(float(label[0, i - 1]))
        except ValueError:
            tipo = "Categorica"
            print("tipo: ", tipo)
            rangeCategoric(i - 1, variable)
            print("------------------------")
        else:
            tipo = "numerico"
            print("tipo: ", tipo)
            rangeNumeric(i - 1, variable)
            print("------------------------")


def getRule(uSoporte=0, uConfianza=0):
    """Obtener las Reglas."""
    for i in range(len(label)):
        for j in range(len(label[i])):
            if type(label[i, j]) != str:
                label[i, j] = str(label[i, j])

    results = list(apriori(label))
    for r in results:
        if(r[1] >= uSoporte):
            print(showLabel(list(r[0])), " SOPORTE: ", r[1])
            for rule in r[2]:
                rule = list(rule)
                if(rule[2] >= uConfianza):
                    print("***", showLabel(list(rule[0])),
                          "-->", showLabel(list(rule[1])),
                          "Confianza:", rule[2],
                          "empuje: ", rule[3])
    print(len(results))
