import numpy as np
import pandas as pd

# === Parameters ===
F = 60         # Futures price
K = 60         # Strike price
r = 0.08       # Risk-free rate (annual)
sigma = 0.30   # Volatility (annual)
T = 0.5        # Time to maturity (in years)
N = 2          # Number of steps in the binomial tree

# === Derived values ===
dt = T / N                         # Length of one time step
u = np.exp(sigma * np.sqrt(dt))   # Up factor
d = 1 / u                          # Down factor
p = 0.5                            # Risk-neutral probability for futures
discount = np.exp(-r * dt)        # Discount factor per step

# === Initialize futures price tree ===
futures_prices = np.zeros((N+1, N+1))  # rows = down moves, cols = time steps
for i in range(N+1):  # Time steps
    for j in range(i+1):  # Down steps
        futures_prices[j, i] = F * (u ** (i - j)) * (d ** j)

# === Initialize option value tree ===
option_values = np.zeros((N+1, N+1))
# Terminal payoffs at t = T
for j in range(N+1):
    option_values[j, N] = max(futures_prices[j, N] - K, 0)

# === Backward induction ===
for i in range(N-1, -1, -1):  # From second-last column to first
    for j in range(i+1):
        hold = discount * (p * option_values[j, i+1] + (1 - p) * option_values[j+1, i+1])
        option_values[j, i] = hold  # No early exercise for European call

# === Output ===
european_call_price = option_values[0, 0]
print(f"European Call Option Price (2-step Binomial Tree) = ${european_call_price:.4f}")

# Optional: Show the binomial trees
futures_df = pd.DataFrame(futures_prices, columns=[f"t={i}" for i in range(N+1)])
option_df = pd.DataFrame(option_values, columns=[f"t={i}" for i in range(N+1)])

print("\nFutures Price Tree:")
print(futures_df)

print("\nOption Value Tree:")
print(option_df)
print("\nConclusion:")
print("For a call option on a futures contract, early exercise is never optimal.")
print("Hence, the value of the American call option is the same as the European one.")