import numpy as np
import matplotlib.pyplot as plt

# Definer funksjonen
def f(x):
    return np.exp(-x/4) * np.arctan(x)

# Verdier for x og y
x = np.linspace(-5, 10, 500)
y = f(x)

# Plot
plt.plot(x, y, label="f(x)")
plt.grid()

plt.plot(1.7777, 0.7069, 'ro', label="Toppunkt")

plt.legend()
plt.show()