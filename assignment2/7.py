import sympy as sp

# Define symbols
x, y, z, t = sp.symbols('x y z t', real=True)
r_sym, h = sp.symbols('r h', real=True)

# 7(a): Average temperature over rectangle
T = 10 - 8*x**2 - 2*y**2
T_avg = (1 / (1*2)) * sp.integrate(sp.integrate(T, (y, 0, 2)), (x, 0, 1))

# 7(b): Line integral along helix
r_vec = sp.Matrix([sp.cos(t), sp.sin(t), t])
f = r_vec[0]*r_vec[1] + r_vec[2]**3
ds_dt = sp.sqrt(sum(sp.diff(r_vec[i], t)**2 for i in range(3)))
line_integrand = f * ds_dt
line_integral = sp.integrate(line_integrand, (t, 0, sp.pi))

# 7(c): Mass of cylinder with density rho = x^2 + y^2 = r^2
theta, r = sp.symbols('theta r', real=True)
polar_rho = r**2
mass_integral = sp.integrate(sp.integrate(sp.integrate(polar_rho * r, (r, 0, r_sym)), (theta, 0, 2*sp.pi)), (z, 0, h))

# 7(d)(i): Check if vector field is conservative
Fx = sp.exp(y)
Fy = x * sp.exp(y)
is_conservative = sp.simplify(sp.diff(Fy, x) - sp.diff(Fx, y)) == 0

# 7(d)(ii): Potential function φ
phi_func = x * sp.exp(y)

# 7(d)(iii): Work done over semicircle from (1,0) to (-1,0)
theta = sp.symbols('theta')
x_circ = sp.cos(theta)
y_circ = sp.sin(theta)
F_circ = sp.Matrix([sp.exp(y_circ), x_circ * sp.exp(y_circ)])
dr_dtheta = sp.Matrix([sp.diff(x_circ, theta), sp.diff(y_circ, theta)])
F_dot_dr = F_circ.dot(dr_dtheta)
work = sp.integrate(F_dot_dr, (theta, 0, sp.pi))

# Display all answers
results = {
    "7(a) Avg Temp": T_avg.simplify(),
    "7(b) Line Integral": line_integral.simplify(),
    "7(c) Mass of Cylinder": mass_integral.simplify(),
    "7(d)(i) Is Conservative?": is_conservative,
    "7(d)(ii) Potential φ(x,y)": phi_func,
    "7(d)(iii) Work (symbolic)": work
}
for k, v in results.items():
    print(f"{k}: {v}")
