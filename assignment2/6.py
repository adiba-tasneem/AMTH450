import sympy as sp
import numpy as np
from scipy.integrate import dblquad, tplquad

# Define symbols
x, y, z, r, theta = sp.symbols('x y z r theta', real=True)

### 6(a)(i) — Hybrid Approach ###
# Symbolic inner integral
inner_expr = x * sp.exp(-z) * sp.cos(z)
inner_int = sp.integrate(inner_expr, (z, 0, 4 - x**2 - y**2)).simplify()
inner_func = sp.lambdify((x, y), inner_int, 'numpy')

# Outer integral numerically
def hybrid_func(y, x):  # Note: dblquad needs (y, x)
    return inner_func(x, y)

def y_lower(x): return 0
def y_upper(x): return 1 - x**2
a1_val, _ = dblquad(hybrid_func, 0, 1, y_lower, y_upper)

### 6(a)(ii) — Symbolic Double Integral ###
integrand_a2 = x * y / sp.sqrt(x**2 + y**2 + 1)
a2_sym = sp.integrate(sp.integrate(integrand_a2, (y, 0, 1)), (x, 0, 1))
a2_val = sp.N(a2_sym)

### 6(b) — Surface Area ###
z_expr = sp.sqrt(4 - x**2)
dz_dx = sp.diff(z_expr, x)
area_integrand = sp.sqrt(1 + dz_dx**2)
area_sym = sp.integrate(sp.integrate(area_integrand, (x, 0, 1)), (y, 0, 4))
area_val = sp.N(area_sym)

### 6(c) — Volume under paraboloid inside shifted cylinder ###
x_sub = r * sp.cos(theta) + 1
y_sub = r * sp.sin(theta)
z_sub = 4 - x_sub**2 - y_sub**2
volume_expr = z_sub * r
volume_sym = sp.integrate(sp.integrate(volume_expr, (r, 0, 1)), (theta, 0, 2 * sp.pi))
volume_val = sp.N(volume_sym)

### Print all results ###
print("6(a)(i) - Triple Integral (hybrid method):")
print("  Symbolic inner integral =", inner_int)
print(f"  Approximate value ≈ {a1_val:.5f}")

print("\n6(a)(ii) - Double Integral:")
print("  Symbolic =", a2_sym)
print(f"  Approximate ≈ {a2_val:.5f}")

print("\n6(b) - Surface Area:")
print("  Symbolic =", area_sym)
print(f"  Approximate ≈ {area_val:.5f}")

print("\n6(c) - Volume:")
print("  Symbolic =", volume_sym)
print(f"  Approximate ≈ {volume_val:.5f}")

