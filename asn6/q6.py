import numpy as np
import matplotlib.pyplot as plt

# Parameters
strike_call = 45
strike_put = 40
premium_call = 3
premium_put = 4
total_cost = premium_call + premium_put

# Range of stock prices at expiry
S = np.linspace(20, 70, 500)

# Payoffs and profits
call_payoff = np.maximum(S - strike_call, 0)
put_payoff = np.maximum(strike_put - S, 0)

call_profit = call_payoff - premium_call
put_profit = put_payoff - premium_put

total_profit = call_profit + put_profit

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(S, total_profit, label='Total Profit', color='blue')
plt.axhline(0, color='black', linestyle='--')
plt.axvline(strike_call, color='red', linestyle=':', label='Call Strike ($45)')
plt.axvline(strike_put, color='green', linestyle=':', label='Put Strike ($40)')
plt.title("Profit Diagram for Long Strangle (Buy Call @45, Put @40)")
plt.xlabel("Stock Price at Expiry ($)")
plt.ylabel("Profit ($)")
plt.grid(True)
plt.legend()
plt.show()
