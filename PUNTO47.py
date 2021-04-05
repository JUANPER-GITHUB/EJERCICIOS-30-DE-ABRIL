# PUNTO 47
print("Digite dos numeros, asegurese de poner primero un numero menor al posterior: ")
n = int(input())
m = int(input())
if m > n:
    for x in range(n, m + 1):
        print(x)
else:
    print("El primer numero que ingresó no es menor al segundo")
