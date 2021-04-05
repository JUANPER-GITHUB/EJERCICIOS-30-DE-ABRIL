# PUNTO 32
x = float(input("Indique cuanta distancia en kilomteros va a recorrer su vuelo: "))
y = int(input("Indique el numero de dias que tendra su estancia: "))
precio = 5000 * x
if precio < 100000:
    precio = 100000
if x > 1000 and y > 7:
    valorpago = precio - (precio * 0.15)
    print("El valor total de su vuelo aplicando un descuento del 15% es de:", valorpago)
else:
    print("El valor total de su vuelo es de:", precio)
