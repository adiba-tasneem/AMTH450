import numpy as np
import matplotlib.pyplot as plt

# Parameters
K = 150      # Strike price
premium = 5  # Premium for all options
S = np.linspace(100, 200, 500)  # Range of stock prices at expiry

# Payoff and Profit calculations

# (a) Long Call
payoff_long_call = np.maximum(S - K, 0)
profit_long_call = payoff_long_call - premium

# (b) Short Call
payoff_short_call = -np.maximum(S - K, 0)
profit_short_call = payoff_short_call + premium

# (c) Long Put
payoff_long_put = np.maximum(K - S, 0)
profit_long_put = payoff_long_put - premium

# (d) Short Put
payoff_short_put = -np.maximum(K - S, 0)
profit_short_put = payoff_short_put + premium


# ---- Subplot helper ----
def plot_option_ax(ax, title, payoff, profit):
    ax.plot(S, payoff, linestyle='--', label='Payoff')
    ax.plot(S, profit, label='Profit')
    ax.axhline(0, linewidth=0.8)
    ax.axvline(K, linestyle=':', label='Strike')
    ax.set_title(title)
    ax.grid(True)
    ax.legend()

# ---- One figure with 4 subplots ----
fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=True, sharey=True)

plot_option_ax(axes[0, 0], "Long Call Option",  payoff_long_call,  profit_long_call)
plot_option_ax(axes[0, 1], "Short Call Option", payoff_short_call, profit_short_call)
plot_option_ax(axes[1, 0], "Long Put Option",   payoff_long_put,   profit_long_put)
plot_option_ax(axes[1, 1], "Short Put Option",  payoff_short_put,  profit_short_put)

# Common labels and tidy layout
fig.supxlabel("Stock Price at Expiry ($)")
fig.supylabel("Payoff / Profit ($)")
fig.tight_layout()
plt.show()
