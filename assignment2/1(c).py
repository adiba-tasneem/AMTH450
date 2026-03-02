import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sin, cos, diff, atan2
import sympy as sp 

# Problem 1(c) - Velocity, acceleration, and angle θ(t)

# Define the curve r(t) = (3t, sin(t), t^2)
t = symbols('t')
r_t = [3 * t, sin(t), t**2]

# Calculate velocity and acceleration as derivatives of r(t)
velocity = [diff(component, t) for component in r_t]
acceleration = [diff(component, t) for component in velocity]

print(f"Velocity vector: {velocity}")
print(f"Acceleration vector: {acceleration}")

# Calculate θ(t) = arctan(vy / vx), where vx and vy are velocity components
vx, vy = velocity[0], velocity[1]
theta_t = atan2(vy, vx)

# Plot θ(t) versus t over the interval [0, 10]

theta_func = sp.lambdify(t, theta_t, 'numpy')

t_values = np.linspace(0, 10, 100)
theta_values = theta_func(t_values)

# Plotting θ(t)
plt.figure(figsize=(10, 6))
plt.plot(t_values, theta_values, label=r"$\theta(t)$", color="purple")
plt.title(r"Plot of $\theta(t)$ versus $t$")
plt.xlabel("t")
plt.ylabel(r"$\theta(t)$ (radians)")
plt.grid(True)
plt.legend()
plt.show()
