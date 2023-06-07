import matplotlib.pyplot as plt
import numpy as py

x = py.array(["A", "B", "C", "D"])
y = py.array([2, 8, 4, 6])

plt.bar(x,y,color="green",width=1.4)
plt.show()
