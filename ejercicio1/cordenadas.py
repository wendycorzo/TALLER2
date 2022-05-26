"""Ejercicio 1:
Programa que lea las coordenadas cartesianas (x, y) de un punto en el plano y
calcule el cuadrante al cual pertenece el punto."""

print("---------------------------------------")
print("-------UBICACION DE CORDENANDAS -------")
print("---------------------------------------")

# input
X= input("Digite el valor de X:")
X= int(X)
Y= input("Digite el valor de Y:")
Y= int(Y)


# processing
if X ==0:
    if Y ==0:
        print("La cordenada es el punto de origen")
    else:
        print("La cordenada esta sobre el eje Y")


else:
    if Y==0:
        print("La cordenada esta sobre el eje X")

    else:
        if X>0:
            if Y>0:
                print("La cordenada esta en el primer cuadrante")

            else:
                print("La cordenada esta en el cuarto cuadrante")
        else:
            if Y<0:
                print("La cordenada es del tercer cuadrante")  

            else:
                print("La cordenada es del segundo cuadrante")              
