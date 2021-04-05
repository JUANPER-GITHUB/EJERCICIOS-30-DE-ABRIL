# PUNTO 48
print("Digite dos numeros, asegurese de poner primero un numero menor al posterior: ")
n = int(input())
m = int(input())
y = 0
contador = (m + 1) - n
if m > n:
    for x in range(n, m + 1):
        y = y + x
        contador = contador - 1
        if contador == 0:
            print(y)
            break
else:
    print("El primer numero que ingresó no es menor al segundo")
