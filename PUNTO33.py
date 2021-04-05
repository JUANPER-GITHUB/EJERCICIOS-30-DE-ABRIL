# PUNTO 33
x = int(input("¿Que año desea saber si es bisieto?"))
if x % 4 == 0 and x % 100 != 0:
    print("El año bisiesto")
else:
    if x % 4 == 0 and x % 100 == 0 and x % 400 == 0:
        print("El año bisiesto")
    else:
        print("El año no es bisiesto")
