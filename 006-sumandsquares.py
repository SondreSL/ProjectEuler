import time
start = time.time()

def squaresum(n):
    total1 = []
    total2 = []
    for i in range(1, n+1):
        total1.append(i)
        total2.append(i**2)
    print("Square of the sum:", (sum(total1))**2)
    print("Sum of the squares:", sum(total2))
    print("Difference:", (sum(total1)**2) - sum(total2))

squaresum(100)
print("{0:.5f} sekunder.".format(time.time() - start))
