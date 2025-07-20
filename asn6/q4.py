import numpy as np

# (a) Initial values
S0 = 40  # Initial stock price
r = 0.10  # Risk-free interest rate
T = 1  # Time to maturity in years

# Forward price at t=0
F0 = S0 * np.exp(r * T)
V0 = 0  # Initial value of the forward contract

print(f"(a) Forward Price at initiation: ${F0:.2f}")
print(f"(a) Initial Value of the contract: ${V0:.2f}")

# (b) After 6 months
t = 0.5  # time passed in years
St = 45  # stock price after 6 months
remaining_time = T - t  # time left until maturity

# Forward price 6 months later
Ft = St * np.exp(r * remaining_time)

# Value of the original contract
Vt = St - F0 * np.exp(-r * remaining_time)

print(f"(b) New Forward Price at t=0.5: ${Ft:.2f}")
print(f"(b) Value of original contract at t=0.5: ${Vt:.2f}")
