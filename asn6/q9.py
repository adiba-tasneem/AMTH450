import numpy as np
from scipy.stats import norm

# Given data
S = 30         # Stock price
K = 29         # Strike price
r = 0.05       # Risk-free rate
sigma = 0.25   # Volatility
T = 4 / 12     # Time to maturity (in years)

# Black-Scholes d1 and d2
d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)

# (a) European Call price
call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

# (b) American Call (same as European for non-dividend stock)
american_call_price = call_price

# (c) European Put price
put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# (d) Put-Call Parity check
lhs = call_price + K * np.exp(-r * T)
rhs = put_price + S
parity_holds = np.isclose(lhs, rhs)

# Print results
print(f"(a) European Call Price: ${call_price:.4f}")
print(f"(b) American Call Price (no dividend): ${american_call_price:.4f}")
print(f"(c) European Put Price: ${put_price:.4f}")
print(f"(d) Put-Call Parity holds: {parity_holds} (LHS={lhs:.4f}, RHS={rhs:.4f})")
