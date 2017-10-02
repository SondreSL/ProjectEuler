def findLetters(n):
    letterCount = 0
    for i in range(1,n):
        c = int(i % 10)
        t = int(((i % 100) - c) / 10)
        h = int(((i % 1000) - (t*10) - c)  / 100)
        if h != 0:
            letterCount += Hundreds+preTwenty[h]
            if c != 0 or t != 0: letterCount += 3 # and
        if t == 0 or t == 1:
            letterCount += preTwenty[c + (t * 10)]
        else:
            letterCount += preTwenty[c]+tens[t]

    return letterCount

preTwenty = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens = [0,3,6,6,5,5,5,7,6,6]
Hundreds = 7
thousand = 8

# total = thousand
# for i in range(1,1000):
#     c = i % 10
#     t = ((i % 100) - c) / 10
#     h = ((i % 1000) - ((c*10)+t) / 100)
    #
    # total  += preTwenty[c]+tens[t]+Hundreds[h]

print(findLetters(1000)+thousand+preTwenty[1])
