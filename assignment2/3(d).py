import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# # Define variables
x, y = sp.symbols('x y')

# # Define the temperature function T(x, y)
T = 3*x**2*y

# # Compute gradient
T_x = sp.diff(T, x)
T_y = sp.diff(T, y)
grad_T = sp.Matrix([T_x, T_y])

# Compute at given point (-1, 3/2)
point = (-1, 3/2)
grad_val = grad_T.subs({x: point[0], y: point[1]})

# Define direction (-1, -1/2) and normalize
direction = np.array([-1, -1/2])
unit_direction = direction / np.linalg.norm(direction)

# Compute directional derivative
directional_derivative = grad_val.dot(sp.Matrix(unit_direction))

# Display results
print("Gradient of T(x,y):", grad_T)
print("Gradient at (-1, 3/2):", grad_val)
print("Directional Derivative:", directional_derivative.evalf())

# Plot directional derivative over region
X = np.linspace(-2, 0, 50)
Y = np.linspace(0, 2, 50)
X, Y = np.meshgrid(X, Y)
Z = 3 * X**2 * Y  # Compute temperature values

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Temperature T(x,y)')
ax.set_title('Directional Derivative Visualization')

plt.show()



