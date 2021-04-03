# PUNTO 24
x = int(input("Ingrese el numero del cual desea saber si es par positivo o par negativo o impar positivo o impar negativo: "))
if x == 0:
    print("¡Cero es un numero neutro!")
else:
    if x % 2 == 0:
        if x > 0:
            print("El numero ingresado es Par Positivo")
        else:
            print("El numero ingresado es Par Negativo")
    else:
        if x > 0:
            print("El numero ingresado es Impar Positivo")
        else:
            print("El numero ingresado es Impar Negativo")
