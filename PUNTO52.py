# PUNTO 52
x = True
while x:
    y = float(input("Digite un numero entero positivo: "))
    if y >= 0 and y % 1 == 0:
        break
    else:
        print("El valor ingresado no es valido, intente nuevamente")
        continue
print(y)
