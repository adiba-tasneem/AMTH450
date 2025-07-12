import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, solve_bvp

def eqs(t, y): return y[1], 100 * y[0]

def bvp_bc(ya, yb): 
    return ya[0] - 1, yb[0] - np.exp(-10)

def shooting_method(h, steps):
    t_eval = np.linspace(0, 1, steps)
    sol1 = solve_ivp(eqs, [0, 1], [1, 0], t_eval=np.linspace(0, 1, steps))
    sol2 = solve_ivp(eqs, [0, 1], [0, 1], t_eval=np.linspace(0, 1, steps))
    phi = (np.exp(-10) - sol1.y[0, -1]) / sol2.y[0, -1]
    return t_eval, sol1.y[0] + phi * sol2.y[0]

t1, y1 = shooting_method(0.1, 11)
t2, y2 = shooting_method(0.05, 21)

plt.plot(t1, y1, label="Shooting Method (h=0.1)")
plt.plot(t2, y2, label="Shooting Method (h=0.05)")

x = np.linspace(0, 1, 100)
y_guess = np.zeros((2, x.size))
sol_bvp = solve_bvp(eqs, bvp_bc, x, y_guess)
plt.plot(sol_bvp.x, sol_bvp.y[0], label="solve_bvp")

plt.legend(), plt.xlabel("x"), plt.ylabel("y")
plt.grid()
plt.show()
