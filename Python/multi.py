def hyper(*lengths):  
    i = iter(lengths)  
    v = next(i)  
    for length in i:  
        v *= length  
    return v  
print(hyper(2, 3, 4, 5))  
