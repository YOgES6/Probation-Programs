import matplotlib.pyplot as plt
import numpy as py

x = py.random.randint(100, size=(100))
y = py.random.randint(100, size=(100))
colors = py.random.randint(100, size=(100))
sizes = 10 * py.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()
