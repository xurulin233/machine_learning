import random

# 定义目标函数
def objective_function(x):
    return -(x ** 2)  # 以负平方作为目标函数（求最大值）

# 爬山算法函数
def hill_climbing(max_iterations, step_size):
    current_solution = random.uniform(-10, 10)  # 随机初始化当前解
    for _ in range(max_iterations):
        neighboring_solution = current_solution + random.uniform(-step_size, step_size)  # 在邻域内随机选择一个解
        if objective_function(neighboring_solution) > objective_function(current_solution):  # 选择比当前解更优的解
            current_solution = neighboring_solution  # 移动到更优的解
    return current_solution

# 调用爬山算法
best_solution = hill_climbing(max_iterations=1000, step_size=0.1)
print("Best solution found:", best_solution)
print("Objective value at the best solution:", objective_function(best_solution))

