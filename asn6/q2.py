import numpy as np

# Given values
C = 8  # annual coupon
F = 100  # face value
T = 5  # years to maturity
r = 0.11  # current continuously compounded yield
r_new = 0.108  # new yield
delta_r = -0.002  # -0.2%

# (a) Bond price at r = 0.11
def bond_price(r):
    price = sum([C * np.exp(-r * t) for t in range(1, T + 1)])
    price += F * np.exp(-r * T)
    return price

price = bond_price(r)

# (b) Duration
def bond_duration(r, price):
    duration = sum([t * (C * np.exp(-r * t)) for t in range(1, T + 1)])
    duration += T * (F * np.exp(-r * T))
    return duration / price

duration = bond_duration(r, price)

# (c) Estimate price change using duration
delta_P = -duration * price * delta_r
new_price_estimate = price + delta_P

# (d) Recalculate bond price at new yield
new_price_actual = bond_price(r_new)

# Display all results
print(f"(a) Bond Price at 11%: {price:.4f}")
print(f"(b) Duration: {duration:.4f} years")
print(f"(c) Estimated Price Change for -0.2% yield: {delta_P:.4f}")
print(f"    Estimated New Price: {new_price_estimate:.4f}")
print(f"(d) Actual New Price at 10.8%: {new_price_actual:.4f}")
