# PUNTO 21
a = int(input("Ingrese un numero de cuatro cifras"))
c1 = a % 10
c2 = int((a % 100) / 10)
c3 = int((a % 1000) / 100)
c4 = int((a - (a % 1000)) / 1000)
print(c1, c2, c3, c4)
