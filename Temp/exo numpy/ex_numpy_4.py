import numpy as np

def mult_array(x,z):
    y = np.dot(x, z, out=None)
    return y

array_1 = np.arange(1,11)

array_2 = np.arange(1,11)

print(mult_array(array_1,array_2))