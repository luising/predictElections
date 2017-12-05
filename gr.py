import numpy as np

a = [[" distrito[CAJEME] puesto[Presidente] partido[PAN] genero[Mujer] " +
      " economia activa[192311-242310] economia inactiva[76987-126987] " +
      " grado de escolaridad[10-11] con religion[359951-459950] sin religion[19860-31859]"]]
c = [
    ["con religion[259951-359950]"],
    ["sin religion[19860-31859]"],
    ["genero[Mujer]", "economia inactiva[76987-126987]"],
    ["genero[Mujer]", "con religion[259951-359950]"],
    ["genero[Mujer]", "sin religion[7859-19859]"],
    ["economia activa[142311-192310]", "con religion[259951-359950]"],
    ["economia inactiva[76987-126987]", "sin religion[7859-19859]"],
    ["con religion[259951-359950]", "grado de escolaridad[6-10]"]
]
c = np.array(c)

print(a[0])
resultado = []
for fila in a:
    temporal = []
    for elemento in c:
        value = np.intersect1d(np.array(elemento), fila)
        if value.size != 0:
            temporal.append(value.tolist())
    resultado.append(temporal)
print(resultado)
