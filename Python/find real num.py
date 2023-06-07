import itertools

p=[-25,-10,-7,-3,2,4,8,10]
d=[]
print(len(p),"\n")


for y,s,l in itertools.combinations(p,3):
    if y+s+l==0:
       d=y,s,l
       print(d)
