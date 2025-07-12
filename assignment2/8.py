import sympy as sp
x, y, z, r, theta, t, phi = sp.symbols('x y z r theta t phi')

#8a
F_xy=sp.Matrix([sp.exp(x)-y*3, sp.cos(y)+x*3])
M,N=F_xy[0],F_xy[1]
dN_dx,dM_dy=sp.diff(N,x),sp.diff(M,y)
integrand=dN_dx-dM_dy
integrand_polar=integrand.subs({x:r*sp.cos(theta),y:r*sp.sin(theta)})
print('\n'*3)


print(f"(a) Work Done: {sp.integrate(integrand_polar*r, (r,0,1), (theta, 0, 2*sp.pi))}")


#8b
F_x=x**2
F_thetaphi=F_x.subs({x:sp.sin(theta)*sp.cos(phi)})
ds=sp.sin(theta) #dtheta dphi
integral =sp.integrate(F_thetaphi * ds, (theta, 0, sp.pi), (phi, 0, 2 * sp.pi))
print(f'(b) Surface integral: {integral}')


#8c
F_xyz=sp.Matrix([x**3, y**3, z**2])
divergence_F = sp.diff(F_xyz[0],x)+sp.diff(F_xyz[1],y)+sp.diff(F_xyz[2],z)
divergence_F_rthetaz= divergence_F.subs({x:r*sp.cos(theta), y:r*sp.sin(theta),z:z})
print(f"(c) Outward Flux: {sp.integrate(divergence_F_rthetaz* r, (z, 0, 2), (r, 0, 3), (theta, 0, 2*sp.pi))}")


#8d
F = sp.Matrix([2*z, 3*x, 5*y])
curl_F = sp.Matrix([sp.diff(F[2], y) - sp.diff(F[1], z),
                    sp.diff(F[0], z) - sp.diff(F[2], x),
                    sp.diff(F[1], x) - sp.diff(F[0], y)])
normal = sp.Matrix([-sp.diff(4 - x**2 - y**2, x), -sp.diff(4 - x**2 - y**2, y), 1])
x_p ,y_p = r * sp.cos(theta), r * sp.sin(theta)
z_p= 4 - x_p*2 - y_p*2
n_polar = normal.subs({x: x_p, y: y_p})
surface_integral = sp.integrate(curl_F.dot(n_polar) * r, (r, 0, 2), (theta, 0, 2*sp.pi))

x_para, y_para, z_para = 2 * sp.cos(t), 2 * sp.sin(t), 0
dt = sp.Matrix([sp.diff(x_para, t), sp.diff(y_para, t), sp.diff(z_para, t)])
F_c = F.subs({x: x_para, y: y_para, z: z_para})
line_integral = sp.integrate(F_c.dot(dt), (t, 0, 2*sp.pi))
print(f"(d) Curl of F:{curl_F}")

print(f"    Surface Integral:{surface_integral}")

print(f"    Line Integral:{line_integral}")

print("     Stokes' Theorem is VERIFIED" if sp.simplify(surface_integral - line_integral) == 0 else "Stokes' Theorem is NOT verified")
