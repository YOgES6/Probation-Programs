def k_permutations(items, n):
    if n==0: 
        yield []
    else:
        for item in items:
            for kp in k_permutations(items, n-1):
                if item not in kp:
                    yield [item] + kp
                    
for kp in k_permutations("syp", 3):
    print(kp) 
