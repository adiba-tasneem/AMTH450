import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

def dsdt(t, s):
    x1, u1, u2, x2, v1, v2 = s
    return [u1, u2, -2*v1**2 + x2, v1, v2, -u2**3 + v1 + x1 + np.sin(t)]

t = np.linspace(0, 1, 100)
s0 = [0, 0, 0, 0, 0, 0]
sol = odeint(dsdt, s0, t, tfirst=True)
plt.plot(t, sol[:, 0], label='x1')
plt.plot(t, sol[:, 3], label='x2')
plt.xlabel('t')
plt.ylabel('x')
plt.title('solution of the system of ode')
plt.legend()
plt.show()