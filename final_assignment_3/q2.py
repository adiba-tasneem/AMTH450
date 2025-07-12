import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def lotka_volterra(z, t):
    x, y = z
    dxdt = -0.1*x + 0.02*x*y
    dydt = 0.2*y - 0.025*x*y
    return [dxdt, dydt]


x0 = 6  
y0 = 6  
z0 = [x0, y0]

t = np.linspace(0, 100, 10000)


sol = odeint(lotka_volterra, z0, t)

plt.figure(figsize=(10, 6))
plt.plot(t, sol[:,0], label='Predators (x(t))', color='red')
plt.plot(t, sol[:,1], label='Prey (y(t))', color='blue')

diff = sol[:, 0] - sol[:, 1]

for i in range(0, len(diff)):
    if diff[i] < 0 and diff[i+1] > 0:  
        t_meet = t[i]
        x_meet = sol[i, 0]
        y_meet = sol[i, 1]
        break


plt.axvline(x=t_meet, color='green', linestyle='--', label=f'First Meeting at t ≈ {t_meet:.2f}')

plt.title('Lotka-Volterra Predator-Prey Model')
plt.xlabel('Time')
plt.ylabel('Population (Thousands)')
plt.legend()
plt.grid()
plt.show()

print(f"Populations first meet at t ≈ {t_meet:.2f}")
print(f"At that time, predator population ≈ {x_meet:.2f} and prey population ≈ {y_meet:.2f}")