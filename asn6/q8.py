import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# === Black-Scholes Pricing Formula ===
def bs_call_price(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)

def bs_put_price(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# === Market Parameters ===
S0 = 32        # Current stock price
r = 0.05       # Risk-free rate
sigma = 0.30   # Volatility
T6m = 0.5      # 6 months
T1y = 1.0      # 1 year

# === Strike Prices ===
strikes = [25, 30, 35]

# === Option Prices ===
call_6m = {K: bs_call_price(S0, K, T6m, r, sigma) for K in strikes}
put_6m = {K: bs_put_price(S0, K, T6m, r, sigma) for K in strikes}
call_1y = {K: bs_call_price(S0, K, T1y, r, sigma) for K in strikes}
put_1y = {K: bs_put_price(S0, K, T1y, r, sigma) for K in strikes}

# === Strategy Costs ===
costs = {
    'Bull Spread (Call)': call_6m[25] - call_6m[30],
    'Bear Spread (Put)': put_6m[30] - put_6m[25],
    'Butterfly (Call, 1y)': call_1y[25] - 2*call_1y[30] + call_1y[35],
    'Butterfly (Put, 1y)': put_1y[25] - 2*put_1y[30] + put_1y[35],
    'Straddle': call_6m[30] + put_6m[30],
    'Strangle': call_6m[35] + put_6m[25],
}

# === Payoff Functions ===
def bull_spread_call(S): return np.maximum(S - 25, 0) - np.maximum(S - 30, 0)
def bear_spread_put(S): return np.maximum(30 - S, 0) - np.maximum(25 - S, 0)
def butterfly_call(S): return np.maximum(S - 25, 0) - 2*np.maximum(S - 30, 0) + np.maximum(S - 35, 0)
def butterfly_put(S): return np.maximum(25 - S, 0) - 2*np.maximum(30 - S, 0) + np.maximum(35 - S, 0)
def straddle(S): return np.maximum(S - 30, 0) + np.maximum(30 - S, 0)
def strangle(S): return np.maximum(S - 35, 0) + np.maximum(25 - S, 0)

# === Final Stock Prices to Display in Table ===
S_display = np.arange(10, 55, 5)

# === Compute Profits for Table ===
strategies = {
    'Bull Spread (Call)': bull_spread_call,
    'Bear Spread (Put)': bear_spread_put,
    'Butterfly (Call, 1y)': butterfly_call,
    'Butterfly (Put, 1y)': butterfly_put,
    'Straddle': straddle,
    'Strangle': strangle,
}

# === Table Data ===
table_data = {'Final Stock Price': S_display}
for name, func in strategies.items():
    table_data[name] = np.round(func(S_display) - costs[name], 2)

# Create and print table
table_df = pd.DataFrame(table_data)
print("Profit Table (Profit vs Final Stock Price):\n")
print(table_df.to_string(index=False))

# === Plotting (Optional) ===
S_range = np.linspace(10, 50, 500)
plt.figure(figsize=(14, 8))
for name, func in strategies.items():
    profit = func(S_range) - costs[name]
    plt.plot(S_range, profit, label=name)
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.title("Profit vs Final Stock Price for Option Strategies")
plt.xlabel("Final Stock Price")
plt.ylabel("Profit")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


