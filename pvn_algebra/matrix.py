import numpy as np
import neutrosophic_number
from neutrosophic_number import NeutrosophicNumber


def add_min(matrix1, matrix2):
    result = np.empty(matrix1.shape, dtype=object)
    for i in range(matrix1.shape[0]):
        for j in range(matrix1.shape[1]):
            result[i, j] = neutrosophic_number.add_min(matrix1[i, j], matrix2[i, j])
    return result


def add_max(matrix1, matrix2):
    result = np.empty(matrix1.shape, dtype=object)
    for i in range(matrix1.shape[0]):
        for j in range(matrix1.shape[1]):
            result[i, j] = neutrosophic_number.add_max(matrix1[i, j], matrix2[i, j])
    return result


def multiply(matrix1, matrix2):
    result = np.empty((matrix1.shape[0], matrix2.shape[1]), dtype=object)
    for i in range(matrix1.shape[0]):
        for j in range(matrix2.shape[1]):
            sum_result = NeutrosophicNumber(0, 0)
            for k in range(matrix1.shape[1]):
                sum_result += neutrosophic_number.multiply(matrix1[i, k], matrix2[k, j])
            result[i, j] = sum_result
    return result


A = np.matrix([
    [NeutrosophicNumber(-8, 1), NeutrosophicNumber(5, -1)],
    [NeutrosophicNumber(3, 8), NeutrosophicNumber(23, -2)]
])

B = np.matrix([
    [NeutrosophicNumber(3, 2), NeutrosophicNumber(13, 3)],
    [NeutrosophicNumber(7, 9), NeutrosophicNumber(3, 5)]
])
print("----------- ADD MIN -----------")
C = add_min(A, B)
print(C, "\n")
print("----------- ADD MAX -----------")
E = add_max(A, B)
print(E, "\n")
print("----------- MULTIPLY -----------")
A = np.matrix([
    [NeutrosophicNumber(-1), NeutrosophicNumber(2), NeutrosophicNumber(indet=-1)],
    [NeutrosophicNumber(3), NeutrosophicNumber(indet=1), NeutrosophicNumber()]
])

B = np.matrix([
    [NeutrosophicNumber(indet=1), NeutrosophicNumber(1), NeutrosophicNumber(2), NeutrosophicNumber(4)],
    [NeutrosophicNumber(1), NeutrosophicNumber(indet=1), NeutrosophicNumber(), NeutrosophicNumber(2)],
    [NeutrosophicNumber(5), NeutrosophicNumber(-2), NeutrosophicNumber(indet=3), NeutrosophicNumber(indet=-1)]
])
E = multiply(A, B)
print(E, "\n")
