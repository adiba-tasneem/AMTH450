import numpy as np

# Payments and years
payments = [460, 235, 640, 370, 330, 250]
years = list(range(1, 7))

# === (1) Continuous Compounding ===
r_continuous = 0.05  # You can change this (e.g., 0.0433 for 4.33%)

pv_continuous = sum([C * np.exp(-r_continuous * t) for C, t in zip(payments, years)])
print(f"Present Value (Continuous Compounding at {r_continuous*100:.2f}%): ${pv_continuous:.2f}")

# === (2) Quarterly Compounding ===
r_quarterly = 0.045  # 4.5% annual interest rate
m = 4  # Compounded quarterly

pv_quarterly = sum([C / (1 + r_quarterly / m) ** (m * t) for C, t in zip(payments, years)])
print(f"Present Value (Quarterly Compounding at 4.5%): ${pv_quarterly:.2f}")
