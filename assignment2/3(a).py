import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def compute_curve_properties(r, t):
    r_prime = r.diff(t)
    r_dprime = r_prime.diff(t)
    
    # TNB frame
    T = r_prime / r_prime.norm()
    B = r_prime.cross(r_dprime) / r_prime.cross(r_dprime).norm()
    N = B.cross(T)
    
    # Curvature
    curvature = r_prime.cross(r_dprime).norm() / (r_prime.norm()**3)
    
    # Torsion
    torsion = T.dot(T.diff(t).cross(T.diff(t).diff(t))) / (T.cross(T.diff(t)).norm()**2)
    
    return {
        'r_prime': r_prime,
        'r_dprime': r_dprime,
        'T': T, 'N': N, 'B': B,
        'curvature': curvature,
        'torsion': torsion
    }

def plot_curvatures(curves_data, t_range=(0, 2*np.pi), num_points=100):
    t_vals = np.linspace(t_range[0], t_range[1], num_points)
    
    plt.figure(figsize=(10, 6))
    
    for name, curvature_func, style in curves_data:
        plt.plot(t_vals, curvature_func(t_vals), style, linewidth=2, label=name)
    
    plt.title('Curvature Comparison')
    plt.xlabel('t')
    plt.ylabel('Curvature')
    plt.legend()
    plt.grid(True)
    plt.show()


# Define parameter
t = sp.symbols('t', positive=True)

# Define curves
ellipse = sp.Matrix([2*sp.cos(t), 3*sp.sin(t), 0])
helix = sp.Matrix([sp.exp(t), sp.exp(t)*sp.cos(t), sp.exp(t)*sp.sin(t)])

# Compute properties
ellipse_props = compute_curve_properties(ellipse, t)
helix_props = compute_curve_properties(helix, t)


# Convert curvatures to numpy functions
k_ellipse = sp.lambdify(t, ellipse_props['curvature'], 'numpy')
k_helix = sp.lambdify(t, helix_props['curvature'], 'numpy')

# Plot curvatures
curves_data = [
    ('Ellipse', k_ellipse, 'b--'),
    ('Helix', k_helix, 'r-')
]

plot_curvatures(curves_data)


