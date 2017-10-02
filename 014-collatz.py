def collatz(n):
    counter = 0
    while n != 1:
        counter += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = (3*n) + 1
    return counter

import time

maks = [0,0]

start = time.time()
for i in range(1,1000):
    c = collatz(i)
    if c > maks:
        maks[0] = c
        maks[1] = i

print("{} has {} terms in {:.4f}.".format(num,maks,time.time()-start))
# print(terms)
