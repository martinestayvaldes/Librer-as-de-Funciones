#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
#Promedio
def promedio(x):
    return sum(x) / len(x)

#Mediana
def mediana(x):
    y = sorted(x)
    n = len(y)
    m = n // 2
    return y[m] if n % 2 else (y[m - 1] + y[m]) / 2

#Moda
def moda(x):
    valores = []
    frecuencias = []

    for v in x:
        if v in valores:
            frecuencias[valores.index(v)] += 1
        else:
            valores.append(v)
            frecuencias.append(1)

    max_f = max(frecuencias)
    return [valores[i] for i in range(len(valores)) if frecuencias[i] == max_f]

#Cuartiles
def cuartiles(x):
    y = sorted(x)
    n = len(y)

    q2 = mediana(y)
    mitad = n // 2

    inferior = y[:mitad]
    superior = y[mitad:] if n % 2 == 0 else y[mitad + 1:]

    q1 = mediana(inferior)
    q3 = mediana(superior)

    return q1, q2, q3

#Percentiles
def percentil(x, p):
    y = sorted(x)
    k = (len(y) - 1) * p / 100
    f = math.floor(k)
    c = math.ceil(k)

    if f == c:
        return y[int(k)]

    return y[f] + (k - f) * (y[c] - y[f])

#Desviacion Estandar
def desviacion_estandar(x):
    mu = promedio(x)
    return math.sqrt(sum((xi - mu) ** 2 for xi in x) / len(x))

#Desviacion absoluta de la mediana
def mad(x):
    m = mediana(x)
    return mediana([abs(xi - m) for xi in x])

#Covarianza
def covarianza(x, y):
    mx = promedio(x)
    my = promedio(y)
    return sum((x[i] - mx) * (y[i] - my) for i in range(len(x))) / len(x)

#Correlacion de Pearson
def correlacion(x, y):
    return covarianza(x, y) / (desviacion_estandar(x) * desviacion_estandar(y))

