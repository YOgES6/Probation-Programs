import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3,4,5,6])
y = np.array([3,7,2,10,4,8,6])

plt.subplot(1,2,1)
plt.plot(x,y,marker='o',color="green")
plt.title("No.1",size=20,color='brown')
plt.xlabel("X-Axis",color='red',size=12)
plt.ylabel("Y-Axis",color='blue',size=12)


x = np.array([0,1,2,3,4,5,6])
y = np.array([10,20,30,40,50,60,70])

plt.subplot(1, 2, 2)
plt.plot(x,y,marker='*',color="green")
plt.title("No.2",size=20,color='brown')
plt.xlabel("X-Axis",color='red',size=12)
plt.ylabel("Y-Axis",color='blue',size=12)
plt.subplots_adjust(wspace=0.4)
plt.show()
