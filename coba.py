import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,101)
y = x**2

plt.plot(x,y)
plt.grid(True)
plt.show() 