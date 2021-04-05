# PUNTO 40
x = int(input("Digite un numero del 1 al 7: "))
if 1 <= x <= 7:
    if x == 1:
        print("LUNES")
    if x == 2:
        print("MARTES")
    if x == 3:
        print("MIERCOLES")
    if x == 4:
        print("JUEVES")
    if x == 5:
        print("VIERNES")
    if x == 6:
        print("SABADO")
    if x == 7:
        print("DOMINGO")
else:
    print("El numero ingresado no esta en el rango entro 1 y 7, vuelvalo a intentar")
