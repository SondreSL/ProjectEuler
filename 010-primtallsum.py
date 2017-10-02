# Project Euler #10

total = [2]

for n in range(3, 20):
    for i in range(2,n+1):
        if i == int((n**0.5))+1:
            print(n)
            total.append(n)
            break
        elif n % i == 0:
            break

print(sum(total))
print(total)
