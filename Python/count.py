def count(firstval=0, step=1):
    x = firstval
    while True:
        yield x
        x += step
        
counter = count() # count will start with 0
for i in range(10):
    print(next(counter), end=", ")

start_value = 2.1
stop_value = 0.4
print("\nNew counter:")
counter = count(start_value, stop_value)
for i in range(10):
    new_value = next(counter)
    print(f"{new_value:2.2f}", end=", ")
