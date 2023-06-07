import mysql.connector
import matplotlib.pyplot as plt
import numpy as py

x = py.array([0,10,20,30,40])
y = py.array([0,30,60,20,80])

font1 = {'family':'serif','color':'blue','size':40}
font2 = {'family':'serif','color':'darkred','size':20}


plt.plot(x,y,'o--r')
plt.title("GRAPH",fontdict=font1)
plt.xlabel("X-Axis",fontdict=font2)
plt.ylabel("Y-Axis",fontdict=font2)
plt.grid(color='green',linestyle='--',linewidth=1.4)
plt.show()
