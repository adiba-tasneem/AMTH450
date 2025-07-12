import sympy as sp

x, y = sp.symbols('x y')

f = y**2 * sp.cos(x - y)

f_x = sp.diff(f, x)
f_y = sp.diff(f, y)

f_xx = sp.diff(f_x, x)
f_yy = sp.diff(f_y, y)

f_xy = sp.diff(f_x, y)
f_yx = sp.diff(f_y, x)

laplace_eq = f_xx + f_yy

print("First Partial Derivatives:")
print("f_x =", f_x)
print("f_y =", f_y)

print("\nSecond Partial Derivatives:")
print("f_xx =", f_xx)
print("f_yy =", f_yy)

print("\nChecking Laplace Equation (f_xx + f_yy):", laplace_eq.simplify())

print("\nChecking Mixed Partial Derivatives:")
print("f_xy =", f_xy)
print("f_yx =", f_yx)
print("Are f_xy and f_yx equal?", sp.simplify(f_xy - f_yx) == 0)

u = sp.re(f)
v = sp.im(f)

if u.diff(x)==v.diff(y) and u.diff(y)==-v.diff(x):
    print('Cauchy-Riemann conditions  satisfied')
else:
    print('Cauchy Riemann conditons not satisfied')