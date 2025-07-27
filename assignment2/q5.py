import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize


def ellipsoid(x, y, z):
    return x**2 + 4*y**2 + z**2 - 18
def gradient(x, y, z):
    return np.array([2*x, 8*y, 2*z])


point = np.array([1, 2, 1])
grad = gradient(*point)
print('\n'*3)
print('-'*140)
print(f'Question - 5')
print('-'*140)
print(f"(i) Equation of the tangent plane: {grad[0]}(x - {point[0]}) + {grad[1]}(y - {point[1]}) + {grad[2]}*(z - {point[2]}) = 0")
print('-'*140)
print(f"(ii) Parametric equations of the normal line: x = {point[0]} + {grad[0]}*t, y = {point[1]} + {grad[1]}*t, z = {point[2]} + {grad[2]}*t")
print('-'*140)


normal_tangent = grad
normal_xy = np.array([0, 0, 1])
cos_theta = np.dot(normal_tangent, normal_xy) / (np.linalg.norm(normal_tangent) * np.linalg.norm(normal_xy))
theta = np.arccos(cos_theta)
acute_angle = min(theta, np.pi - theta)
print(f"(iii) Acute angle between the tangent plane and the xy-plane: {acute_angle} radians")
print('-'*140)
print('(iv) Visualization:')


u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.sqrt(18) * np.outer(np.cos(u), np.sin(v))
y = np.sqrt(18/4) * np.outer(np.sin(u), np.sin(v))
z = np.sqrt(18) * np.outer(np.ones(np.size(u)), np.cos(v))
fig = plt.figure(figsize=(12, 10))  
fig.patch.set_facecolor('lightblue')  
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('lightblue') 
ellipsoid_surface = ax.plot_surface(x, y, z, cmap='plasma', alpha=0.7)
xx, yy = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))
zz = (-grad[0]*(xx - point[0]) - grad[1]*(yy - point[1]) + grad[2]*point[2]) / grad[2]
tangent_plane = ax.plot_surface(xx, yy, zz, color='lightblue', alpha=0.5)


t = np.linspace(-5, 5, 100)
x_line = point[0] + grad[0]*t
y_line = point[1] + grad[1]*t
z_line = point[2] + grad[2]*t
normal_line, = ax.plot(x_line, y_line, z_line, color='black', linewidth=2)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14, labelpad=10)  
ax.view_init(elev=35, azim=45)  
ax.legend([ellipsoid_surface, tangent_plane, normal_line], 
          ['Ellipsoid', 'Tangent Plane', 'Normal Line'], 
          loc='upper left', fontsize=12)
plt.show()


def ellipsoid_constraint(x):
    return 4*x[0]*2 + x[1]*2 + 4*x[2]*2 - 16
def temperature(x):
    return 8*x[0]**2 + 4*x[1]*x[2] - 16*x[2] + 600
constraint = {'type': 'eq', 'fun': ellipsoid_constraint}
result = minimize(lambda x: -temperature(x), [1, 1, 1], constraints=constraint)
hottest_point = result.x
print('-'*140)
print("(b) Hottest point on the surface:", hottest_point)
print('-'*140)
