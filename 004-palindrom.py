a = 0
liste = []
telle = 0

for i in range(100,1000):
    for n in range(i,1000):
        k = i * n
        telle += 1
        if str(k) == (str(k)[::-1]):
            print(i, n, i*n)
            liste.append([i*n, i, n])
            if k > a: a = k

# print(*liste, sep="\n") # Printer listen med alle elementene på ny linje.
print(max(liste)) # Printer bare det siste elementet i listen, som er det høyeste (så lenge bare 900+ er med
print(len(liste))
# print(telle)
# print(a)






# (n[::-1]) # Reverses a string
