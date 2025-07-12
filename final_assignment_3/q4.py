import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy.integrate import odeint
def dsdt(t, s, a):
    x, u = s
    return [u, -a*np.sin(x)]

a = 32.17/2
x0 = np.pi/6
u0 = 0
s0 = [x0, u0]
t = np.linspace(0, 2, 200)
sol = odeint(dsdt, y0=s0, t=t, tfirst=True, args=(a,))
plt.plot(t, sol[:, 0], label='x(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('x')
plt.grid()
plt.show()