from scipy.optimize import minimize
def objective(x):
    return x**2 + 4
result = minimize(objective, x0=5)
print("Minimum Value at:", result.x)
print("Minimum Function Value:", result.fun)
