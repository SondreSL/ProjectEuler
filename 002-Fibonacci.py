

def fib(n): # Set the upper n.
    total = []
    n = int(n)
    a, b = 0, 1
    while a < n:
#        print(a)
        a, b = b, a+b # Surprisingly simple.
        if a % 2 == 0:
            total.append(a)
    print(sum(total))


fib(4000000)

# Ikke veldig pent ...
