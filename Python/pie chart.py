import matplotlib.pyplot as plt
import numpy as py

y=py.array([30,25,20,25]) 
mylabels=["Study","Dress","Extra","Food"]
myexplode=[0.1,0.1,0.1,0.1]

plt.pie(y,labels=mylabels,explode=myexplode,shadow=True)
plt.legend(title="Expensive:")
plt.show()
