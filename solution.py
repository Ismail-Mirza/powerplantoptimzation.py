


from pulp import LpProblem, LpMinimize, LpVariable, lpSum,LpStatus

def optimize_power_plant_operations(n, m, p, cost_matrix, capacity_matrix):
    prob = LpProblem("PowerPlantOptimization", LpMinimize)

    x = {(i, j): LpVariable(name=f"x_{i}_{j}", cat="Binary") for i in range(1, n + 1) for j in range(1, m + 1)}

    prob += lpSum(cost_matrix[i-1][j-1] * x[i, j] for i in range(1, n + 1) for j in range(1, m + 1))

    prob += lpSum(capacity_matrix[i-1][j-1] * x[i, j] for i in range(1, n + 1) for j in range(1, m + 1)) >= p, "PowerDemandConstraint"

    prob.solve()
    # print(prob)

    if LpStatus[prob.status] == 'Optimal':
        print("Optimal Solution Found:")
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                print(f"Unit {j} in Power Plant {i}: {'On' if x[i, j].value() == 1 else 'Off'}")
    else:
        print("No optimal solution found.")

# Example usage
n = 3 
m = 2  
p = 100  

cost_matrix = [
    [10, 15],
    [12, 14],
    [11, 13]
]

capacity_matrix = [
    [30, 40],
    [25, 35],
    [20, 30]
]

optimize_power_plant_operations(n, m, p, cost_matrix, capacity_matrix)
