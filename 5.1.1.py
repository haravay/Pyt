import numpy as np

a = 0.94
x = 0.093
z = np.arccos(x**2) - a * (np.sqrt(x)) + (np.sin(np.pi/2 + 2)**3) / np.log2(x)
print(z)