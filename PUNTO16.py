# PUNTO 16
import math
x1 = float(input("Digite el valor de x en la coordenada 1: "))
y1 = float(input("Digite el valor de y en la coordenada 1: "))
x2 = float(input("Digite el valor de x en la coordenada 2: "))
y2 = float(input("Digite el valor de x en la coordenada 2: "))
distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)
print("La distancia entre los dos puntos del plano cartesiano es:", distancia)
