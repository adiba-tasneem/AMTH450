import numpy as np

# Given data
cash_flows_A = [225, 215, 250, 225, 205]
cash_flows_B = [220, 225, 250, 250, 210]
r = 0.0433  # continuously compounded annual interest rate

# Compute present value using continuous discounting: PV = C * exp(-rt)
def present_value(cash_flows, rate):
    return sum([C * np.exp(-rate * t) for t, C in enumerate(cash_flows, start=1)])

pv_A = present_value(cash_flows_A, r)
pv_B = present_value(cash_flows_B, r)

print(f"Present Value of Investment A: {pv_A:.2f}")
print(f"Present Value of Investment B: {pv_B:.2f}")

# Determine preferable investment
if pv_A > pv_B:
    print("Investment A is preferable.")
elif pv_B > pv_A:
    print("Investment B is preferable.")
else:
    print("Both investments are equally preferable.")
