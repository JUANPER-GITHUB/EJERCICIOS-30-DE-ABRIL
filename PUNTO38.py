# PUNTO 38
print("Ingrese 3 numeros")
x = float(input())
y = float(input())
z = float(input())
if x < y < z:
    print("Los numeros estan aumentando")
else:
    if x > y > z:
        print("Los numeros estan disminuyendo")
    else:
        print("No se incrementa ni se disminuye")
