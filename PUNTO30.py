# PUNTO 30
print("Ingrese tres numeros: ")
x = float(input())
y = float(input())
z = float(input())
if x > y:
    m = x
else:
    m = y
if m > z:
    mayor = m
else:
    mayor = z
if x < y:
    min = x
else:
    min = y
if min < z:
    minimo = min
else:
    minimo = z
print("El numero menor es:", minimo)
print("El numero mayor es:", mayor)
