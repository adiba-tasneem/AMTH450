import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.integrate import odeint


def competition_model(t, z):
    x, y = z
    dxdt = x * (2 - 0.4*x - 0.3*y)
    dydt = y * (1 - 0.1*y - 0.3*x)
    return [dxdt, dydt]


x_vals = np.linspace(-1, 10, 20)
y_vals = np.linspace(-1, 12, 20)
X, Y = np.meshgrid(x_vals, y_vals)
U = X * (2 - 0.4*X - 0.3*Y)
V = Y * (1 - 0.1*Y - 0.3*X)


M = np.hypot(U, V)
M[M == 0] = 1 
U /= M
V /= M


initial_points = [(1.5, 3.5), (1, 1), (2, 7), (4.5, 0.5)]
t_span = [0, 100]  
t_eval = np.linspace(0, 50, 300)  


plt.figure()

plt.quiver(X, Y, U, V, color='b', alpha=0.5)


for x0, y0 in initial_points:
    sol = solve_ivp(competition_model, t_span, [x0, y0], t_eval=t_eval)
    plt.plot(sol.y[0], sol.y[1], label=f"Start: ({x0}, {y0})")
    plt.plot(x0, y0, 'ro', markersize=6)
    plt.plot(sol.y[0,-1], sol.y[1,-1], 'bo', markersize=6, )
    plt.text(sol.y[0,-1], sol.y[1,-1], f'({sol.y[0,-1]:.0f}, {sol.y[1,-1]:.0f})', fontsize=10, ha='left', color='black')
    
    
plt.plot(0.5, 6, 'go', markersize=8, label="Equilibrium (0.5, 6)")


plt.xlabel("x (Population 1)")
plt.ylabel("y (Population 2)")
plt.title("Vector Field and Trajectories of the Competition Model")
plt.xlim(-0.5, 5.5)
plt.ylim(-0.5, 10.5)
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(12, 8))
plt.title("Population vs Time for Different Initial Conditions", fontsize=16, y=1.03)

for i, (x0, y0) in enumerate(initial_points):
    sol = solve_ivp(competition_model, t_span, [x0, y0], t_eval=t_eval)
    
    plt.subplot(2, 2, i + 1)
    plt.plot(t_eval, sol.y[0], label="Prey")
    plt.plot(t_eval, sol.y[1], label="Predator")
    plt.title(f"Initial: ({x0}, {y0})")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.grid(True)
    plt.legend()

plt.tight_layout()

plt.show()
