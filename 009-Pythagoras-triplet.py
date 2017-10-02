def pytho():
    for i in range(1,333):
        for n in range(i+1,600):
            trippel = (i**2) + (n**2)
            print(i, n)
            if i + n + trippel**0.5 == 1000:
                print(i, n, "{0:.0f}".format(trippel**0.5))
                return

pytho()
