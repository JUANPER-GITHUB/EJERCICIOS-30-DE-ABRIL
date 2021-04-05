# PUNTO 31
print("Ingrese tres numeros: ")
x = float(input())
y = float(input())
z = float(input())
if x + y == z:
    print("La suma de los dos primero numeros es IGUAL al tercer numero")
else:
    if x + y > z:
        print("La suma de los dos primero numeros es MAYOR al tercer numero")
    else:
        print("La suma de los dos primero numeros es MENOR al tercer numero")
