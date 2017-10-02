import time
start = time.time()

total = [2]


for n in range(3, 105000):
    m = 0
    for i in total:
        if i > n**0.5:
            #print(n)
            total.append(n)
            break
        elif n % total[m] == 0:
            break
        else:
            m += 1

# print(sum(total))
print(len(total))
print(total[10001]) # Printer primtall nr 10 000
print(time.time() - start)
