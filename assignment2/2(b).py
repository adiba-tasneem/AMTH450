import numpy as np
import matplotlib.pyplot as plt

# Helix path: r(t) = (cos(t), sin(t), t)
t_values = np.linspace(0, 10, 100)
x = np.cos(t_values)
y = np.sin(t_values)
z = t_values

# Plot the helix
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label="Helix: r(t) = (cos(t), sin(t), t)", color="blue")
ax.scatter(1, 0, 0, color="red", label="Start point (1, 0, 0)")

# Labels and legend
ax.set_title("Helix and Bug's Path")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()
plt.show()
