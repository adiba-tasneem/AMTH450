import numpy as np
import pandas as pd

M = 1e5

A = np.array([

    [200, 100, -1, 0, 0, 1, 0, 0],  
    [1,   2,   0, -1, 0, 0, 1, 0],  
    [40,  40,  0, 0, -1, 0, 0, 1]   
], dtype=float)


b = np.array([4000, 50, 1400], dtype=float)

C = np.array([4, 3, 0, 0, 0, M, M, M], dtype=float)

BV = [5, 6, 7]  # a1, a2, a3
Cb = C[BV].copy()


tableau = np.hstack([A, b.reshape(-1, 1)]).astype(float)

var_names = [f"x{i+1}" for i in range(2)] + [f"s{i-1}" for i in range(2,5)] + [f"a{i-4}" for i in range(5,8)]

iteration = 0
while True:
    print(f"\nIteration {iteration}:")
    print("-----------------------")

   
    Zj = np.dot(Cb, tableau[:, :-1])
    Zj_Cj = Zj - C

    
    full_table = np.hstack([tableau[:, :-1], tableau[:, [-1]]])
    display_cols = var_names + ["RHS"]
    df = pd.DataFrame(full_table, columns=display_cols)
    df.index = [f"B{i+1} ({var_names[BV[i]]})" for i in range(len(BV))]
    df.loc["Zj - Cj"] = list(np.round(Zj_Cj, 2)) + [""]

    print(df)

    
    if all(Zj_Cj[i] <= 0 for i in range(len(Zj_Cj)) if i not in BV):
        break

    
    entering_index = np.argmax(Zj_Cj)
    print(f"Entering Variable: {var_names[entering_index]}")

    
    col = tableau[:, entering_index]
    ratios = []
    for i in range(len(col)):
        if col[i] > 0:
            ratios.append(tableau[i, -1] / col[i])
        else:
            ratios.append(np.inf)

    leaving_index = np.argmin(ratios)
    print(f"Leaving Variable: {var_names[BV[leaving_index]]}")

    
    pivot_element = tableau[leaving_index, entering_index]
    tableau[leaving_index, :] /= pivot_element

    for i in range(len(tableau)):
        if i != leaving_index:
            tableau[i, :] -= tableau[i, entering_index] * tableau[leaving_index, :] 

    
    if var_names[BV[leaving_index]].startswith('a'):
        print(f"Removing Artificial Variable: {var_names[BV[leaving_index]]}")

        
        tableau = np.delete(tableau, BV[leaving_index], axis=1)
        C = np.delete(C, BV[leaving_index])
        var_names.pop(BV[leaving_index])

        
        if entering_index > BV[leaving_index]:
            entering_index -= 1
        BV = [v-1 if v > BV[leaving_index] else v for v in BV]

    
    BV[leaving_index] = entering_index
    Cb[leaving_index] = C[entering_index]

    iteration += 1


solution = np.zeros(len(var_names))
for i, var_index in enumerate(BV):
    solution[var_index] = tableau[i, -1]


original_cost = 4 * solution[0] + 3 * solution[1]

print("\nOptimal Solution :")
for i in range(2):  
    print(f"x{i+1} = {solution[i]}")
print(f"Minimum Cost = {original_cost}")