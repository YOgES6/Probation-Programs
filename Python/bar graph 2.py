import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "P", "C", "D","E", "S", "Y"])
y = np.array([3, 8, 1, 10, 6, 8, 5])



font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':12}

plt.title("Bar Graph", fontdict = font1)
plt.xlabel("X-Axis", fontdict = font2)
plt.ylabel("Y-Axis", fontdict = font2)

plt.plot(x, y)
plt.show()
