def prim_fakt(n):
    tall = n
    while tall > 1:
        for i in range(2, int((n**0.5)+1)):
            if tall % i == 0:
                faktorer.append(i)
                tall = tall / i
                break






# def primfakt(n):
#     for i in range(2, int((n**0.5)+1)):
#         if n / i == 1:
#             faktorer.append(n)
#         elif n % i == 0:
#             faktorer.append(i)
#             if n > 0:
#                 primfakt(n/i)
#             if n == 1:
#                 faktorer.append(i)
#             return


faktorer = []
# primfakt(1)
# primfakt(13195)
# print(primfakt(13195))
# primfakt(600851475143)

# primfakt(int(input("Hvilket tall vil du ha primfaktoreren til?\n> ")))
prim_fakt(int(input("Hvilket tall vil du ha primfaktoreren til?\n> ")))

print(faktorer)
