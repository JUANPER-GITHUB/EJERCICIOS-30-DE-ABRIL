# PUNTO 27
n1 = float(input("¿Cual es el valor de la nota 1?"))
n2 = float(input("¿Cual es el valor de la nota 2?"))
n3 = float(input("¿Cual es el valor de la nota 3?"))
n4 = float(input("¿Cual es el valor de la nota 4?"))
n5 = float(input("¿Cual es el valor de la nota 5?"))
final = (n1 * 0.15) + (n2 * 0.20) + (n3 * 0.15) + (n4 * 0.30) + (n5 * 0.20)
if final < 2:
    print("El estudiante No puede habilitar la materia")
if final < 3:
    print("El estudiante Reprobó la materia")
if final >= 3:
    print("El estudiante Aprobó la materia")
if final > 4.5:
    print("¡Felicitación al estudiante por la excelente nota en la materia!")
