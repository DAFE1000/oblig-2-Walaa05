import numpy as np
from scipy.optimize import fsolve

# Definer funksjonene
def f(x):
    return np.exp(-x/4) * np.arctan(x)

def g(x):
    return np.arctan(x) - 4/(x**2 + 1)

# Finn toppunktet
x_topp = fsolve(g, 1.8)[0]
y_topp = f(x_topp)

print(f"Toppunkt: ({x_topp:.4f}, {y_topp:.4f})")