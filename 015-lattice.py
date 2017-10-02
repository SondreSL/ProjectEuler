# Find the number of possible permutations one can go from top left to bottom right in
# a 20x20 grid, by only moving right and down.

# Need to right 20 times and down 20 times.

def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i-1]
    return L[cube_size - 1]

n = route_num(20)
print("{}".format(n))
