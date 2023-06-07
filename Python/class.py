memo = {0:0, 1:1}
def fib(n):
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

def fib_index(*x):
    """ finds the natural number i with fib(i) == n """
    if len(x) == 1:
        # started by user
        # find index starting from 0
        return fib_index(x[0], 0)
    else:
        n = fib(x[1])
        m = x[0]
        if  n > m:
            return -1
        elif n == m:
            return x[1]
        else:
            return fib_index(m, x[1]+1)


# code from the previous example with the functions fib() and find_index()

print(" index of a |    a |     b   |sum of squares| index ")	
print("=====================================================")
for i in range(15):
    square = fib(i)**2 + fib(i+1)**2
    print(f"{i:12d}|{fib(i):6d}|{fib(i+1):9d}|{square:14d}|{fib_index(square):5d}")
