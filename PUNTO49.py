# PUNTO 49
x = True
contador = 10
s = 0
while x:
    y = int(input("Porfavor ingrese un numero: "))
    s = s + y
    contador = contador - 1
    if contador == 0:
        break
p = s /10
print("La suma de todos los valores ingresados es:", s)
print("El promedio de todos los valores ingresados es:", p)
