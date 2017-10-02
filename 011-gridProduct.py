grid = open("011.txt", "r") # Aapner 011.txt med alle tallene i.
lister = []                 # Lager en liste til tallene.


for line in grid:           # Henter alle linjene i .txt filen
    lister.append(line[:-1])     # Legger alt i listen 'lister'


grid.close()

M = [l.split() for l in lister]         # MR CLEAN
M = [[int(j) for j in i] for i in M]

# print(M)

storst = 0

# Horisontalt først:

for i in range(20):
    for j in range(16):
        prod = M[i][j]*M[i][j+1]*M[i][j+2]*M[i][j+3]  # Horisontalt
        if prod > storst:
            storst = prod
            print("Horisontalt", i, j)
        prod = M[j][i]*M[j+1][i]*M[j+2][i]*M[j+3][i]  # Vertikalt
        if prod > storst:
            storst = prod
            print("Vertikalt", i, j)

for i in range(16):
    for j in range(16):
        prod = M[i][j]*M[i+1][j+1]*M[i+2][j+2]*M[i+3][j+3]
        if prod > storst:
            storst = prod
            print("Diagonal ned", i, j)

for i in range(19, 4, -1):
    for j in range(16):
        prod = M[i][j]*M[i-1][j+1]*M[i-2][j+2]*M[i-3][j+3]
        if prod > storst:
            storst = prod
            print("Diagonalt opp", i, j)

print(storst)
