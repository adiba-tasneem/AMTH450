import sympy as sp

# Define variable
t = sp.symbols('t')

# Define x, y, z
x = sp.cos(t)
y = sp.sin(t)
z = sp.tan(t)

# Define w
w = sp.sqrt(x**2 + y**2 + z**2)

# Differentiate w with respect to theta
dw_dtheta = sp.diff(w, t)

# Evaluate at θ = π/4
result = dw_dtheta.subs(t, sp.pi/4)

print("dw/dθ:", dw_dtheta.simplify())
print("Value at θ = π/4:", result.evalf())
