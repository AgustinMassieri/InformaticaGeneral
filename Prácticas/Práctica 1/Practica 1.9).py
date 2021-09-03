
def main():

    numero= input("Ingrese numero de cantidad impar de cifras (al menos 3 cifras) :")
    cifras=len(numero)
    primera= numero[0]
    med=numero[(len(numero)-1)//2]
    ultima= numero [len(numero)-1]


    print=input("El numero ingresado tiene {} cifras.".format(cifras))
    print=input(("La primera cifra es {}, la ultima es {} y la central es {}.".format (primera,ultima,med)))
main()


