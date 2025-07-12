import numpy as np
from scipy.integrate import odeint 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def dydt(y,t):
    return 1 + (t - y) ** 2
y0=1
t= np.linspace(2,3,100)
y1= odeint(dydt, y0, t)

sol= solve_ivp(dydt,(2,3),[1], t_eval=t)
y2=sol.y[0]

def exact(t):
    return t + 1 / (1 - t)

exact_y=exact(t)
print("time    exact value       odeint_value    error_odeint    solve_ivp_value   error_solve_ivp" )
for i in range(len(t)):
    error_ode= np.abs(y1[i,0]-exact_y[i]) 
    error_solivp= np.abs(y2[i]-exact_y[i]) 
    print(f"{t[i]:.3f}   {exact_y[i]:.10f}     {y1[i,0]:.10f}     {error_ode:.10f}    {y2[i]:.10f}      {error_solivp:.10f}") 

plt.plot(t,y1,'r', label="ode_int")
plt.plot(t,y2, 'c--', label="solve_ivp")
plt.plot(t, exact_y, 'b:', label="exact soln")
plt.xlabel("t")
plt.ylabel("y")
plt.grid(True, color='gray', linestyle='--', linewidth=0.5)
plt.show()
