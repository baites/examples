import numpy as np
from numpy.linalg import matrix_power
from scipy.linalg import inv, dft, circulant
import matplotlib.pyplot as canvas


#phi = np.exp(-4j * np.pi * np.arange(12) / 12)

#steps = np.array((2,2,1,2,2,2,1,2,2,1,2,2))
steps = np.array((12,12,12,12,12,12,12,12,12,12,12,12))
steps = np.array((1,1,1,1,1,1,1,1,1,1,1,1))
steps = np.array((2,2,2,2,2,2,6,-6,6,-6,6,-6))
#steps = np.array((2,2,1,2,2,2,1,12,12,12,12,12))
#phi = np.exp(-2j * np.pi * np.arange(12) * steps / 12)

#phi[1] = 0
#phi[3] = 0
#phi[6] = 0
#phi[8] = 0
#phi[10] = 0

#0 1 2 3 4 5 6 7 8 9 A B
#1 2 3 4 5 6 7 8 9 10 11 12
#  |   |     |   |     |  |

print(phi)

_, plot = canvas.subplots()

plot.scatter(phi.real, phi.imag)
canvas.show()

print()
mdft = inv(dft(12))

c = mdft @ phi
#for v in c:
#    print(v)

cm = circulant(c)

b = np.zeros(12)
b[1] = 1

print(cm.dot(b))