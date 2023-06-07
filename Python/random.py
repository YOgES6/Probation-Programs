import random
import numpy

def random_ones_and_zeros():
    p = 0.5
    while True:
          x = random.random()
          message = yield 1 if x < p else 0
          if message != None:
             p = message
            

x = random_ones_and_zeros()
next(x) 

for p in[0.2, 0.8]:
    print("\nWe change the probability to : " + str(p))
    x.send(p)    
    for i in range(20):
        print(next(x), end=" ")

