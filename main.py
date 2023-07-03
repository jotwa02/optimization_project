import numpy as np

arr=np.array([1,2,3,4])
np.save('arr.csv',arr,delimiter=',',fmt='%f')
"""Q = 0.03
epsilon = 31536 * 2.72 * 0.7
gamma = 0.113
A = 334
B = 374
n = 0.011
N = 1

def calculate_cost(L):
    cz1 = pow(((54.9 * epsilon * pow(n, 2)) / (gamma * 1.35 * B)), (1 / (1.35 + 5.33)))
    cz2 = pow(Q, (3 / (1.35 + 5.33)))
    D = cz1 * cz2

    I = (A + B * pow(D, N)) * L

    return I

# Przykładowe wartości L
values_of_L = [1, 2, 3, 4]

# Obliczanie i wyświetlanie wartości dla pojedynczych L
for L in values_of_L:
    cost = calculate_cost(L)
    print("Dla L =", L, ", koszt wynosi:", cost)"""