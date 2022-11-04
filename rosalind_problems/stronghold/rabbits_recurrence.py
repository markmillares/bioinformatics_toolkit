def fib_loop(months, offsprings): 
    parent, child = 1, 1
    for i in range(months - 1):
        child, parent = parent, parent + (child * offsprings)
    return child

n = 29
k = 5

print(fib_loop(n,k))