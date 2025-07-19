import numpy as np
import matplotlib.pyplot as plt

# Parameters
K = 150      # Strike price
premium = 5  # Premium for all options
S = np.linspace(100, 200, 500)  # Stock prices at expiry

# Dictionary to hold all options and their formulas
options = {
    "Long Call": {
        "payoff": np.maximum(S - K, 0),
        "profit": np.maximum(S - K, 0) - premium
    },
    "Short Call": {
        "payoff": -np.maximum(S - K, 0),
        "profit": -np.maximum(S - K, 0) + premium
    },
    "Long Put": {
        "payoff": np.maximum(K - S, 0),
        "profit": np.maximum(K - S, 0) - premium
    },
    "Short Put": {
        "payoff": -np.maximum(K - S, 0),
        "profit": -np.maximum(K - S, 0) + premium
    }
}

# Plot using loop in a 2x2 grid
fig, axs = plt.subplots(2, 2, figsize=(8,6))
fig.suptitle('Payoff and Profit Diagrams for Basic Options (K = $150, Premium = $5)', fontsize=16)

# Flatten axs for easy looping
axs = axs.flatten()

# Loop over each option and subplot
for i, (name, data) in enumerate(options.items()):
    axs[i].plot(S, data["payoff"], label='Payoff', linestyle='--')
    axs[i].plot(S, data["profit"], label='Profit', color='green')
    axs[i].axhline(0, color='black', linewidth=0.5)
    axs[i].axvline(K, color='red', linestyle=':', label='Strike Price')
    axs[i].set_title(name)
    axs[i].set_xlabel('Stock Price at Expiry ($)')
    axs[i].set_ylabel('Payoff / Profit ($)')
    axs[i].legend()
    axs[i].grid(True)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

