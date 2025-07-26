import numpy as np

# Given data
S = 19               # Current stock price
K = 20               # Strike price
T = 4 / 12           # Time to maturity in years (4 months)
r = 0.03             # Risk-free interest rate (annual, continuously compounded)
C = 1                # Price of the European call option

# Put-call parity formula: P = C + K*e^(-rT) - S
discounted_strike = K * np.exp(-r * T)
P = C + discounted_strike - S

# Display result
print(f"Price of the 4-month European put option: ${P:.4f}")
