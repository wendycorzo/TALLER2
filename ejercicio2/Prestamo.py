"""Ejercicio 2:
Programa que permita realizar un préstamo bancario, teniendo en cuenta que
el préstamo será otorgado solamente a personas con ingresos superiores
a $945200 y que no posea ninguna otra deuda."""

print("-----------------------------------------------")
print("---------PRESTAMO  APROBADO & DENEGADO --------")
print("-----------------------------------------------")

# input
I= input("Digite el valor de sus ingresos:")
I= int(I)

# processing

if I>945200:
    D= input("Tiene otras deudas Y(1)/N(0): ")
    D=int(D)

    if D==2:
        print("El prestamo ha sido aprobado")

    else:
        print("El prestamo ha sido negado")    


else:
    print("El prestamo ha sido negado")
