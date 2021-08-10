import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Essendo che non ho ben compreso cosa dovevo far tornare come valore la informo che nel caso non fosse corretto
# quello che ho messo per far tornare la lista basta semplicemente sostituire np.array([]) con []
# e rimuovere le voci repr() ma non il loro contenuto.


# Esercizio 1
#
# Scrivere una funzione linear_regr(dataset,value).
# La funzione applica la regressione lineare al dataset e restituisce il valore
# previsto in caso di input value. Si supponga che il dataset contenga
# esclusivamente due colonne di valori: la prima colonna
# corrisponde ai valori di x e la seconda colonna ai valori di y.
#
# Si utilizzino come iperparametri i valori:
# alpha=0.01
# N di iterazioni= 1000
#
# Per esempio, applicando la regressione lineare vista in laboratorio al dataset delle
# biciclette con su un valore di x=0.22 i numero di biciclette noleggiate sarà circa di
# 3733.69.


def linear_regr(dataset, value):

    iterations = 1000
    alpha = 0.01

    if not os.path.isfile(dataset):

        return 0

    data = pd.read_csv(dataset, header = 0)
    data.head()
    data.insert(0, 'Ones', 1)
    columns = data.shape[1]

    x_value = data.iloc[:, 0 : columns - 1]
    x_index = np.matrix(x_value.values)
    y_value = data.iloc[:, columns - 1 : columns]
    y_index = np.matrix(y_value.values)

    theta = np.matrix(np.array([0, 0]))
    figure = np.matrix(np.zeros(theta.shape))
    param = int(theta.ravel().shape[1])
    cost = np.zeros(iterations)

    for element in range(iterations):

        error = (x_index * theta.T) - y_index

        for index in range(param):

            term_molti = np.multiply(error, x_index[:, index])
            x_len = len(x_index)
            figure[0, index] = theta[0, index] - ((alpha / x_len) * np.sum(term_molti))

        theta = figure

    return_elem = theta[0, 0] + (theta[0, 1] * value)
    return return_elem

print(linear_regr("day_mod.csv", 0.22))
# Esercizio 2
#
# Scrivere una funzione vertical_stack(a,b) che sfruttando le
# potenzialità del modulo numpy concatena verticalmente i
# due array a e b restituendo un nuovo array.
#
# Esempio:
# >>> a
# [1, 2, 3]
# >>> b
# [7, 8, 9]
# ….
# array([[1, 2, 3], [7, 8, 9]])


def vertical_stack(a,b):

    if (np.shape(a) != np.shape(b)) or (type(a) != type(np.array([]))) or (type(b) != type(np.array([]))) or len(a) != len(b):

        return np.array([])

    merge_stack = repr(np.vstack((a, b)))

    return merge_stack


# Esercizio 3
#
# Scrivere una funzione match(a,b) che sfruttando le
# potenzialità del modulo numpy restituisce la lista delle
# posizioni in cui gli elementi di a e b sono uguali.
#
# Esempio:
# >>> a
# [1, 8, 6, 3, 5, 6, 4, 6, 1, 7]
# >>> b
# [8, 8, 6, 1, 2, 6, 4, 3, 0, 2]
# >>>
# …
# (array([1, 2, 5, 6]),)


def match(a,b):

    array_list = np.array([])

    if (np.shape(a) != np.shape(b)) or (type(a) != type(np.array([]))) or (type(b) != type(np.array([]))) or (len(a) != len(b)):

        return np.array([])

    for element in range(len(a)):

        elem_compare = np.equal(a[element], b[element])

        if elem_compare:

            array_list = np.append(array_list, element).astype(int)

    return repr(array_list)
