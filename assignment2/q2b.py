import sympy as sp 
import numpy as np 
import matplotlib.pyplot as plt

t = sp.symbols('t', real=True)
u = sp.symbols('u', real=True)
r = sp.Matrix([sp.cos(t),sp.sin(t), t])
tangent = sp.diff(r,t)
s = sp.integrate(tangent.norm(), (t, 0, u)).simplify()
print(f'The arc length parameterization s(t) = {s.subs(u, t)}')

u = sp.solve(sp.symbols('s', real=True) - s, u)[0]
print(f'The circular helix  = {r.subs(t, u)}')

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
t = np.linspace(0,10,1000)
x = np.cos(t)
y = np.sin(t)
z = t

ax.plot(x,y,z,label=" Bug's path ")
ax.plot(x[0],y[0],z[0],'ro',label='t=0')
ax.plot(x[-1],y[-1],z[-1],'go',label='t=10')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Curve C in 3D')
plt.show()