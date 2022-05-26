"""Ejercicio 3:
Programa que le indique el precio de venta
de un articulo dado."""

print("-------------------------------------------------------")
print("---------PRECIO VENTA Y GANACIA DE UN PRODUCTO --------")
print("-------------------------------------------------------")

# input
C=float(input("Digite el precio costo del producto: "))


# processing

if C<3000:
    G=0.15*C

else:
    if C<=6000:
        G=500

    else:
        G=0,25*C


P=C+G

# output

print("\nResultado\n")

print( " El precio venta es : " + str (P) )
print( " El precio de costo es : " + str (C) )
print( " La ganacia es : " + str (G) )