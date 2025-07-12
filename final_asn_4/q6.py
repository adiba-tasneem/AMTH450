import numpy as np
import pandas as pd


costs = np.array([
    [16, 20, 12],
    [14, 8, 18],
    [26, 24, 16]
])

supply = [200, 160, 90]
demand = [180, 120, 150]

def north_west_corner_method(supply, demand):
    m, n = len(supply), len(demand)
    allocation = np.full((m, n), np.nan)
    s = supply.copy()
    d = demand.copy()
    
    i = j = 0
    while i < m and j < n:
        alloc = min(s[i], d[j])
        allocation[i][j] = alloc
        s[i] -= alloc
        d[j] -= alloc
        
        if s[i] == 0:
            i += 1
        elif d[j] == 0:
            j += 1

    return allocation

def display_table(allocation, title):
    print(f"\n=== {title} ===")
    df = pd.DataFrame(allocation, columns=["W1", "W2", "W3"], index=["F1", "F2", "F3"])
    print(df.fillna('-'))

def calculate_total_cost(allocation, costs):
    total = 0
    for i in range(len(costs)):
        for j in range(len(costs[0])):
            if not np.isnan(allocation[i][j]):
                total += allocation[i][j] * costs[i][j]
    return total


def modi_method(costs, allocation):
    m, n = costs.shape
    alloc = allocation.copy()

    while True:
        
        u = [None] * m
        v = [None] * n
        u[0] = 0
        while True:
            updated = False
            for i in range(m):
                for j in range(n):
                    if not np.isnan(alloc[i][j]):
                        if u[i] is not None and v[j] is None:
                            v[j] = costs[i][j] - u[i]
                            updated = True
                        elif v[j] is not None and u[i] is None:
                            u[i] = costs[i][j] - v[j]
                            updated = True
            if not updated:
                break
        
        
        delta = np.full((m, n), np.nan)
        for i in range(m):
            for j in range(n):
                if np.isnan(alloc[i][j]):
                    delta[i][j] = costs[i][j] - (u[i] + v[j])

        
        if np.nanmin(delta) >= 0:
            print("\n Optimality reached!")
            break
        
        
        i_min, j_min = np.unravel_index(np.nanargmin(delta), delta.shape)
        print(f"\n Most negative Δ at ({i_min}, {j_min}) = {delta[i_min][j_min]}")

        
        rows, cols = [], []
        for k in range(n):
            if not np.isnan(alloc[i_min][k]) and k != j_min:
                cols.append(k)
        for k in range(m):
            if not np.isnan(alloc[k][j_min]) and k != i_min:
                rows.append(k)
        
        found = False
        for row in rows:
            for col in cols:
                if not np.isnan(alloc[row][col]):
                    i1, j1 = i_min, j_min
                    i2, j2 = i_min, col
                    i3, j3 = row, col
                    i4, j4 = row, j_min
                    found = True
                    break
            if found:
                break
        
        if not found:
            print("No closed loop found — complex case!")
            break
        
      
        theta = min(alloc[i2][j2], alloc[i3][j3], alloc[i4][j4])
        print(f"θ = {theta}")

        alloc[i1][j1] = 0 if np.isnan(alloc[i1][j1]) else alloc[i1][j1]
        alloc[i1][j1] += theta
        alloc[i2][j2] -= theta
        alloc[i3][j3] += theta
        alloc[i4][j4] -= theta

        
        for i in range(m):
            for j in range(n):
                if alloc[i][j] == 0:
                    alloc[i][j] = np.nan

    return alloc, delta


initial_alloc = north_west_corner_method(supply, demand)
display_table(initial_alloc, "Initial Allocation (North-West Corner Method)")
initial_cost = calculate_total_cost(initial_alloc, costs)
print(f"\nInitial Total Cost = {initial_cost}")

optimal_alloc, delta = modi_method(costs, initial_alloc)
display_table(optimal_alloc, "Final Allocation After MODI Correction")
optimal_cost = calculate_total_cost(optimal_alloc, costs)
print(f"\nOptimal Total Cost = {optimal_cost}")