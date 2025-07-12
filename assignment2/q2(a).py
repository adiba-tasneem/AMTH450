import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t = sp.symbols('t')
r = sp.Matrix([5*sp.cos(t), 4*sp.sin(t)])

# Position vectors
r1 = r.subs(t, np.pi/4).evalf()
r2 = r.subs(t, np.pi).evalf()

#tangent vectors
t1 = sp.diff(r, t).subs(t, np.pi/4).evalf()
t2 = sp.diff(r, t).subs(t, np.pi).evalf()

t_vals = np.linspace(0, 2*np.pi, 100)
r_func = sp.lambdify(t, r, 'numpy')
r_vals = np.array([r_func(t) for t in t_vals])

# Plot 
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(r_vals[:, 0], r_vals[:, 1], label='Curve', color='blue')
ax.plot(0, 0, 'k*', label = 'Origin (0,0)', markersize = 10)
ax.quiver(0, 0, float(r1[0]), float(r1[1]), scale=1, color='cyan', label='r(π/4)', linewidth=2, scale_units='xy', angles='xy')
ax.quiver(0, 0, float(r2[0]), float(r2[1]), scale=1, color='magenta', label='r(π)', linewidth=2, scale_units='xy', angles='xy')
ax.quiver(float(r1[0]), float(r1[1]), float(t1[0]), float(t1[1]), scale=20, color='red', label='Tangent at r(π/4)')
ax.quiver(float(r2[0]), float(r2[1]), float(t2[0]), float(t2[1]), scale = 20, label = 'Tangent at r(pi)', color = 'skyblue')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Parametric Curve with Tangent Vectors')
ax.set_aspect('equal', adjustable='box')
plt.grid()
plt.legend(loc = 'upper left')
plt.show()

