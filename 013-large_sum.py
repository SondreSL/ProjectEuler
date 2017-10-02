# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers. (I 013.txt)

import time

def hentTall(filnavn):
    tall = []
    with open(filnavn) as fil:
        tall = [int(line) for line in fil]
    return tall

start = time.time()

tall = (hentTall("013.txt"))
summ = (str(sum(tall)))
print("{} in {:.10f} seconds".format(summ[:10],time.time() - start))
