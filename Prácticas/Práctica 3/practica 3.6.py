def par (a):
    if a>0:
        if a%2==0:
            b=int(input("Ingrese un numero menor que {}:".format(a)))
            if b>a:
                print("Incorrecto!")
            else:
                print("Correcto!")

        else:
            b=int(input("Ingrese un numero mayor que (a):"))
            if b<a:
                print("Incorrecto!")
            else:
                print("Correcto!")
    else:
        print("Numero ingresado no valido")

def main ():
    a=int(input("Ingrese un numero entero positivo: "))
    b=par(a)
main()