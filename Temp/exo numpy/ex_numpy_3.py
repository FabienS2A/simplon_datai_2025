import numpy as np

def somme_arr(x):
    liste = array.tolist()
    y = 0
    for n in liste :
        y = n + y
    return y

array = np.arange(1,11)

print(array)

print(somme_arr(array))