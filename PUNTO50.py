# PUNTO 50
x = True
contador = 0
s = 0
while x:
    y = int(input("Porfavor ingrese un numero: "))
    s = s + y
    contador = contador + 1
    g = input("¿Desea seguir calculando?, si no quiere seguir escriba 'No' ")
    if g == "No":
        break
p = s / contador
print("La suma de todos los valores ingresados es:", s)
print("El promedio de todos los valores ingresados es:", p)
