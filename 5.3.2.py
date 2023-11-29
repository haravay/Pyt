import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)

X, Y = np.meshgrid(x, y)

z = np.power(np.abs(X), 0.25) + np.power(np.abs(Y), 0.25)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plt.contourf(X, Y, z, levels=20, cmap='viridis')
plt.colorbar()
plt.title('z = x^2 - y^2')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

z = 2 * X + 3 * Y

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plt.contourf(X, Y, z, levels=20, cmap='viridis')
plt.colorbar()
plt.title('z = 2x + 3y')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

z = np.power(X, 2) + np.power(Y, 2)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plt.contourf(X, Y, z, levels=20, cmap='viridis')
plt.colorbar()
plt.title('z = x^2 + y^2')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

z = 2 + 2 * X + 2 * Y - np.power(X, 2) - np.power(Y, 2)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plt.contourf(X, Y, z, levels=20, cmap='viridis')
plt.colorbar()
plt.title('z = 2 + 2x + 2y - x^2 - y^2')
plt.xlabel('x')
plt.ylabel('y')
plt.show()