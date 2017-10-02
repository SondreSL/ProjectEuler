import time

def toThePower(n):
    print("2 to the power {} is {}".format(n, 2**n))
    return 2**n

def sumOfDigits(n):
    total = 0
    n = str(n)
    for i in n:
        total += int(i)
    return total

tall = int(input("Find the power digit sum of 2^n:\n> "))

start = time.time()
s = toThePower(tall)
answer = sumOfDigits(s)

print("{} in {} seconds".format(answer, time.time() - start))
