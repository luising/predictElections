"""Clase Apriori."""
import numpy as np
from apyori import apriori
from matplotlib.pylab import hist, show
from prettytable import PrettyTable

label = []
listLabel = []
Listcategoric = []
listRules = []




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
    """Mostrar el valor de la etiqueta."""
    cadena = ""
    for co in tlabel:
        coc = int(co[0])
        cof = int(co[1])
        cadena += " " + listLabel[coc][cof]
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


def toStringLabel():
    """Covertir en string las etiquetas."""
    for i in range(len(label)):
        for j in range(len(label[i])):
            if type(label[i, j]) != str:
                label[i, j] = str(label[i, j])


def getRule(uSoporte=0, uConfianza=0, pVariable="nan"):
    """Obtener las Reglas."""
    global listRules
    toStringLabel()
    # matriz que guarda reglas,soporte ,confianza
    # obtener combinatoria
    results = list(apriori(label))
    for combinacion in results:
        if(combinacion[1] >= uSoporte):
            for rule in combinacion[2]:
                rule = list(rule)
                if(rule[2] >= uConfianza):
                    if pVariable != "nan":
                        rulep2 = showLabel(list(rule[1]))
                        if pVariable in rulep2:
                            # agregar un nueva regla
                            fRule = (showLabel(list(rule[0])),
                                     showLabel(list(rule[1])))
                            # primer rule , soporte, confianza , empuje
                            ruleDetalle = [fRule, combinacion[1],
                                           rule[2], rule[3]]
                            listRules.append(ruleDetalle)
    listRules = np.array(listRules)


def showRule():
    """Mostrar en tabla."""
    global listRules
    listRules.sort(axis=0)
    x = PrettyTable()
    x.field_names = ["Reglas", "Soporte", "Confianza", "Empuje"]
    for i in range(len(listRules)):
        frule = listRules[i][0][0] + "-->" + listRules[i][0][1]
        row = [frule, listRules[i][1],
               listRules[i][2], listRules[i][3]]
        x.add_row(row)
    print(x)
    # print(showLabel(list(r[0])), " SOPORTE: ", r[1])
    # print("***", showLabel(list(rule[0])),
    #       "-->", showLabel(list(rule[1])),
    #       "Confianza:", rule[2],
    #       "empuje: ", rule[3]).


def showHistogram(atributo):
    """Mostrar histograma."""
    listAtributo = listRules[:, atributo]
    listAtributodif = np.unique(listAtributo)
    print(listAtributo)
    print(len(listAtributodif))
    hist(listAtributo, listAtributodif, rwidth=0.8)
    show()
