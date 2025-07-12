#3
from pulp import LpMaximize, LpProblem, LpVariable
problem = LpProblem("Simplex_Method", LpMaximize)
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
problem += 12 * x1 + 15 * x2 + 14 * x3, "Objective"
problem += x1 + x2 + x3 <= 100, "Constraint 1"
problem += 3 * x1 + 2 * x2 + 5 * x3 <= 3, "Constraint 2"
problem += 0.02 * x1 + 0.04 * x2 + 0.03 * x3 <= 0.03, "Constraint 3"
status = problem.solve()
print(f"Optimal value of Z: {problem.objective.value()}")
print(f"x1 = {x1.value()}")
print(f"x2 = {x2.value()}")
print(f"x3 = {x3.value()}")

#4
from pulp import LpMinimize, LpProblem, LpVariable, lpSum
problem = LpProblem("Minimum_Cost_Food_Mix", LpMinimize)
A = LpVariable("Food_A", lowBound=0)  
B = LpVariable("Food_B", lowBound=0)  
M = 1e6  
artificial1 = LpVariable("Artificial1", lowBound=0)
artificial2 = LpVariable("Artificial2", lowBound=0)
artificial3 = LpVariable("Artificial3", lowBound=0)
problem += 4 * A + 3 * B + M * (artificial1 + artificial2 + artificial3), "Total Cost"
problem += 200 * A + 100 * B + artificial1 >= 4000, "Vitamins"
problem += A + 2 * B + artificial2 >= 50, "Minerals"
problem += 40 * A + 40 * B + artificial3 >= 1400, "Calories"
status = problem.solve()
print(f"Optimal cost: {problem.objective.value()}")
print(f"Food A (units): {A.value()}")
print(f"Food B (units): {B.value()}")

#q5
import numpy as np
supply = [80, 60, 40, 20]
demand = [60, 60, 30, 40, 10]
allocation = np.zeros((4, 5), dtype=int)  
i, j = 0, 0
while i < 4 and j < 5:
    quantity = min(supply[i], demand[j])  
    allocation[i][j] = quantity
    supply[i] -= quantity
    demand[j] -= quantity
    if supply[i] == 0: i += 1  
    if demand[j] == 0: j += 1  
print("North-West Corner Allocation:")
print(allocation)



supply = [80, 60, 40, 20]
demand = [60, 60, 30, 40, 10]
cost_matrix = np.array([
    [4, 3, 1, 2, 6],
    [5, 2, 3, 4, 5],
    [3, 5, 6, 3, 2],
    [2, 4, 4, 5, 3]
])
allocation = np.zeros((4, 5), dtype=int) 
supply=np.array(supply)
demand=np.array(demand)
while supply.sum() and demand.sum():
    cost = np.where((supply[:, None] > 0) & (demand > 0), cost_matrix, np.inf)
    i, j = np.unravel_index(np.argmin(cost), cost.shape)
    qty = min(supply[i], demand[j])
    allocation[i, j] = qty
    supply[i] -= qty
    demand[j] -= qty
print("\nLeast Cost Allocation:")
print(allocation)