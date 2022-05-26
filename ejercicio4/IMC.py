"""Ejercicio 4:
Programa que calcule el índice de masa corporal de una persona"""

print("----------------------")
print("--------- IMC --------")
print("----------------------")

# input
P=float(input("Digite su peso corporal: "))
A=float(input("Digite su altura en metros: "))

# processing

IMC=P/(A*A)

# output

print("\nSu IMC es: \n" + str (IMC)  )


if IMC<16:
    print("Su diagnostico es:" + "Infrapeso")

else:
    if IMC>=17 and IMC<18:
        print("Su diagnostico es:" + "Bajo peso")

    else:
        if IMC>=18 and IMC<25:
            print("Su diagnostico es:" + "Peso normal (saludable)")

        else:
            if IMC>25 and IMC<30:
                print("Su diagnostico es:" + "Sobrepeso (Obesidad de grado I)")

            else:
                if IMC>=30 and IMC<35:
                    print("Su diagnostico es:" + "Sobrepeso cronico (Obecidad de grado II)")

                else:
                    if IMC>=35 and IMC<40:
                        print("Su diagnostico es:" + "Obesidad premorbida (Obesidad de grado III)")
                    else:
                        print("Su diagnostico es:" + "Obesidad morbida (Obecidad  de grado IV")      

