# PUNTO 25
x = int(input("¿Cual es el valor de la compra?"))
iva = x * 0.19
if x >= 150000:
    print("El valor final de la compra con el 5% de descuento es:", x - (x * 0.05))
    print("El valor del iva antes del descuento es:", iva)
else:
    print("El valor final de la compra es:", x)
    print("La compra al no ser mayor o igual a 150.000 no tiene ningun descuento")
