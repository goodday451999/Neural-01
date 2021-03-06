from math import exp
#import numpy
import numpy as np
from numpy import dot

def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    else:
        return 1 / (1 + np, exp(-x))


# Input Data
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# Output Data
Y = np.array([[0],
              [1],
              [1],
              [0]])

np.random.seed(1)

# Synapses
syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

# traning step
for j in range(60000):

    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    l2_error = Y - l2

    if (j % 10000) == 0:
        print("Error: " + str(np.mean(np.abs(l2_error))))

    l2_delta = l2_error * nonlin(l2, deriv=True)  # Backpropagation

    l1_error = l2_delta.dot(syn1.T)

    l1_delta = l1_error * nonlin(l1, deriv=True)

    # update weights
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)  # Gradient Descent

print("Output after traning")
print(l2)
