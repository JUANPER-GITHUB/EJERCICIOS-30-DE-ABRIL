# PUNTO 36
x = int(input("Digite un numero del 0 al 10: "))
if 0 <= x <= 10:
    if x == 0:
        print("CERO")
    if x == 1:
        print("UNO")
    if x == 2:
        print("DOS")
    if x == 3:
        print("TRES")
    if x == 4:
        print("CUATRO")
    if x == 5:
        print("CINCO")
    if x == 6:
        print("SEIS")
    if x == 7:
        print("SIETE")
    if x == 8:
        print("OCHO")
    if x == 9:
        print("NUEVE")
    if x == 10:
        print("DIEZ")
else:
    print("El numero ingresado no esta en el rango entro 0 y 10, vuelvalo a intentar")
