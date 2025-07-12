import numpy as np
import matplotlib.pyplot as plt

# Define x and y ranges
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Define functions
F1 = 4*X**2 + Y**2  # f(x,y) = 4x² + y²
F2 = X**2 + Y**2  # Used for 3D surface visualization

# Contour levels
levels = [1, 4, 9, 16, 26, 36]

# Plot contour for f(x,y)
plt.figure(figsize=(8, 6))
contour1 = plt.contour(X, Y, F1, levels=levels, cmap='coolwarm')
plt.clabel(contour1, inline=True, fontsize=8)
plt.title("Contour Plot of f(x,y) = 4x² + y²")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar()
plt.grid()
plt.show()

from mpl_toolkits.mplot3d import Axes3D

# Define Z range
z = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)  # Extracting z from given equation

# 3D Surface Plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_title("3D Surface Plot of f(x,y,z) = z² - x² - y²")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()

