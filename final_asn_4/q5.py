import pandas as pd
import numpy as np


costs = [
    [4, 3, 1, 2, 6],
    [5, 2, 3, 4, 5],
    [3, 5, 6, 3, 2],
    [2, 4, 4, 5, 3]
]

supply = [80, 60, 40, 20]
demand = [60, 60, 30, 40, 10]

def print_iteration(allocation, step, method_name):
    df = pd.DataFrame(allocation, columns=['P', 'Q', 'R', 'S', 'T'], index=['A', 'B', 'C', 'D'])
    print(f"\n--- {method_name}: Iteration {step} ---")
    print(df.fillna('-'))

def display_allocation(allocation, method_name, costs):
    df = pd.DataFrame(allocation, columns=['P', 'Q', 'R', 'S', 'T'], index=['A', 'B', 'C', 'D'])
    print(f"\n=== {method_name} Final Allocation Table ===")
    print(df.fillna('-'))
    
    # Calculate total cost
    total_cost = 0
    for i in range(4):
        for j in range(5):
            if not np.isnan(allocation[i][j]):
                total_cost += allocation[i][j] * costs[i][j]
    print(f"Total Transportation Cost = {total_cost}")

def north_west_corner(costs, supply, demand):
    allocation = [[np.nan for _ in range(5)] for _ in range(4)]
    supply = supply.copy()
    demand = demand.copy()
    
    i = j = 0
    step = 1
    while i < 4 and j < 5:
        alloc = min(supply[i], demand[j])
        allocation[i][j] = alloc
        supply[i] -= alloc
        demand[j] -= alloc
        
        print_iteration(allocation, step, "North-West Corner Rule")
        step += 1
        
        if supply[i] == 0:
            i += 1
        elif demand[j] == 0:
            j += 1
    return allocation

def least_cost_method(costs, supply, demand):
    allocation = [[np.nan for _ in range(5)] for _ in range(4)]
    supply = supply.copy()
    demand = demand.copy()
    
    used = [[False for _ in range(5)] for _ in range(4)]
    step = 1
    
    while any(s > 0 for s in supply) and any(d > 0 for d in demand):
        
        min_val = float('inf')
        min_pos = (-1, -1)
        for i in range(4):
            for j in range(5):
                if not used[i][j] and supply[i] > 0 and demand[j] > 0:
                    if costs[i][j] < min_val:
                        min_val = costs[i][j]
                        min_pos = (i, j)
        
        i, j = min_pos
        alloc = min(supply[i], demand[j])
        allocation[i][j] = alloc
        supply[i] -= alloc
        demand[j] -= alloc
        
        print_iteration(allocation, step, "Least Cost Method")
        step += 1
        
        if supply[i] == 0:
            for k in range(5):
                used[i][k] = True
        if demand[j] == 0:
            for k in range(4):
                used[k][j] = True
                
    return allocation

#  North-West Corner Rule
nw_allocation = north_west_corner(costs, supply, demand)
display_allocation(nw_allocation, "North-West Corner Rule", costs)

#  Least Cost Method
lc_allocation = least_cost_method(costs, supply, demand)
display_allocation(lc_allocation, "Least Cost Method", costs)
