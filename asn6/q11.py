import numpy as np

# Inputs
S0 = 484
K = 480
r = 0.10
q = 0.03
sigma = 0.25
T = 1/6  # 2 months = 1/6 year
N = 4    # 4 half-month steps

# Step size
dt = T / N
u = np.exp(sigma * np.sqrt(dt))
d = 1 / u
p = (np.exp((r - q) * dt) - d) / (u - d)
discount = np.exp(-r * dt)

# Stock price tree
stock = np.zeros((N+1, N+1))
for i in range(N+1):
    for j in range(i+1):
        stock[j, i] = S0 * (u ** (i - j)) * (d ** j)

# Option value tree
option = np.zeros((N+1, N+1))
# Terminal payoff
for j in range(N+1):
    option[j, N] = max(K - stock[j, N], 0)

# Backward induction with early exercise
for i in range(N-1, -1, -1):
    for j in range(i+1):
        expected = discount * (p * option[j, i+1] + (1 - p) * option[j+1, i+1])
        exercise = max(K - stock[j, i], 0)
        option[j, i] = max(expected, exercise)  # American: take max

# Final result
print(f"Estimated value of the American put option: ${option[0,0]:.4f}")
