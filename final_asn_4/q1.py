
import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 10, 400)
x2 = np.linspace(0, 10, 400)
X1, X2 = np.meshgrid(x1, x2)

constraints = [
    (X1 + 2*X2 <= 10),
    (X1 + X2 <= 6),
    (X1 - X2 <= 2),
    (X1 - 2*X2 <= 1),
    (X1 >= 0),
    (X2 >= 0)
]

feasible_region = np.logical_and.reduce(constraints)

Z = 2*X1 + X2

Z_feasible = np.where(feasible_region, Z, np.nan)

plt.figure()
contour = plt.contourf(X1, X2, Z_feasible, cmap='Blues', levels=100)
#plt.colorbar(contour, label='Objective Function Value (Z)')

plt.plot(x1, (10 - x1) / 2, label='x1 + 2x2 ≤ 10')
plt.plot(x1, 6 - x1, label='x1 + x2 ≤ 6')
plt.plot(x1, x1 - 2, label='x1 - x2 ≤ 2')
plt.plot(x1, (x1 - 1) / 2, label='x1 - 2x2 ≤ 1')
plt.xlim((0, 5))
plt.ylim((0, 5))
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Feasible Region and maximum of objective function (Z= 2x1 + x2)')
plt.legend()


points = [
    (0, 0),
    (0, 3),        
    (2, 4),         
    (4, 2),         
    (3, 3),        
    (4, 0),         
]

points = np.array(points)
z_values = 2 * points[:, 0] + points[:, 1]
max_index = np.argmax(z_values)
optimal_point = points[max_index]
optimal_value = z_values[max_index]


plt.plot(optimal_point[0], optimal_point[1], 'ro', markersize=5)
plt.text(optimal_point[0] + 0.3, optimal_point[1], f'Max Z={optimal_value}', fontsize=10, color='black')

plt.grid()
plt.show(), optimal_point, optimal_value