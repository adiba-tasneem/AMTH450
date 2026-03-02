from sympy import symbols, cos, sin, pi, diff

# Define the curve
t = symbols('t')
r_t = [5 * cos(t), 4 * sin(t)]

# Calculate the tangent vectors (derivative of r(t))
r_prime_t = [diff(component, t) for component in r_t]

# Tangent vectors at t = π/4 and t = π
tangent_vector_pi_4 = [component.subs(t, pi / 4) for component in r_prime_t]
tangent_vector_pi = [component.subs(t, pi) for component in r_prime_t]

print(f"Tangent vector at t = π/4: {tangent_vector_pi_4}")
print(f"Tangent vector at t = π: {tangent_vector_pi}")