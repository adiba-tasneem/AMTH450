import numpy as np

def print_tableau(tableau, basic_vars, var_names, step):
    print(f"\n Step {step} - Tableau:")
    header = var_names + ["RHS"]
    row_labels = basic_vars + ["-Z"]

    # Print header
    print("       " + "  ".join(f"{name:>6}" for name in header))
    for i, row in enumerate(tableau):
        row_str = "  ".join(f"{val:>6.2f}" for val in row)
        print(f"{row_labels[i]:>5} | {row_str}")
    print("-" * 70)

def simplex(c, A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    c = np.array(c, dtype=float)

    m, n = A.shape
    var_names = [f"x{i+1}" for i in range(n)] + [f"s{i+1}" for i in range(m)]
    basic_vars = [f"s{i+1}" for i in range(m)]

    tableau = np.zeros((m+1, n+m+1))
    tableau[:m, :n] = A
    tableau[:m, n:n+m] = np.eye(m)
    tableau[:m, -1] = b
    tableau[-1, :n] = -c

    step = 0
    print_tableau(tableau, basic_vars, var_names, step)

    while any(tableau[-1, :-1] < 0):
        step += 1
        pivot_col = np.argmin(tableau[-1, :-1])
        ratios = [row[-1] / row[pivot_col] if row[pivot_col] > 0 else float('inf') for row in tableau[:-1]]
        pivot_row = np.argmin(ratios)

        # Normalize the pivot row
        tableau[pivot_row] /= tableau[pivot_row, pivot_col]

        # Eliminate other rows
        for i in range(len(tableau)):
            if i != pivot_row:
                tableau[i] -= tableau[i, pivot_col] * tableau[pivot_row]

        basic_vars[pivot_row] = var_names[pivot_col]
        print_tableau(tableau, basic_vars, var_names, step)

    solution = np.zeros(n)
    for i, var in enumerate(basic_vars):
        if var in var_names[:n]:
            solution[var_names.index(var)] = tableau[i, -1]

    max_profit = tableau[-1, -1]
    return solution, max_profit

# Input
c = [12, 15, 14]
A = [
    [3, 2, 5],
    [2, 4, 3],
    [1, 1, 1]
]
b = [3, 3, 100]

# Solve
solution, max_profit = simplex(c, A, b)

# Output
print("\n Final Solution:")
print(f"Coal A: {solution[0]:.3f} tons")
print(f"Coal B: {solution[1]:.3f} tons")
print(f"Coal C: {solution[2]:.3f} tons")
print(f"Maximum Profit: BDT {max_profit:.3f}")