# PUNTO 46
contador1 = 1
contador2 = -2
x = True
n = int(input("Digita el limite al cual quiere que llegue la sucesión de numeros: "))
n = n + 1
print(contador1)
print(contador2)
while x:
    contador1 = contador1 + 2
    contador2 = contador2 - 2
    if contador1 == n:
        break
    else:
        print(contador1)
    if contador2 * -1 == n:
        break
    else:
        print(contador2)
