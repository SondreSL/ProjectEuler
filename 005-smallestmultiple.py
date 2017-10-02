liste = [11, 12, 13, 14, 16, 17, 18, 19, 20]
liste2 = [1,2,3,4,5,6,7,8,9,10]
# Trenger ikke sjekke alle tallene.

i = 2520 # Trenger ikke starte lavere.

while True:
    i += 2520   #
    if all(i % k == 0 for k in liste):
        print(i)
        break
