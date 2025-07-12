import numpy as np
import matplotlib.pyplot as plt

# Define new ranges
x = np.linspace(1, 7, 100)
y = np.linspace(0, 2*np.pi, 100)
X, Y = np.meshgrid(x, y)

# Define functions
F1 = Y**2 - 2*Y*np.cos(X)
F2 = np.abs(np.sin(X) * np.sin(Y))

# Plot first function
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, F1, cmap='plasma')

ax.set_title("3D Plot of f(x,y) = y² - 2y cos(x)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("f(x,y)")
plt.show()

# Plot second function
x = np.linspace(0, 2*np.pi, 100)
y = np.linspace(0, 2*np.pi, 100)
X, Y = np.meshgrid(x, y)
F2 = np.abs(np.sin(X) * np.sin(Y))

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, F2, cmap='coolwarm')

ax.set_title("3D Plot of f(x,y) = |sin(x) sin(y)|")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("f(x,y)")
plt.show()
