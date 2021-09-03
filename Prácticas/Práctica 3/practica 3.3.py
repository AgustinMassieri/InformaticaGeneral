def analisis(a):
    if a>0 and a-int(a)==0:
        print("El numero es positivo y entero")

    if a>0 and a-int(a)!=0:
        print("El numero es positivo y real")

    if a<0 and a-int(a)==0:
        print("El numero es negativo y entero")
        
    if a<0 and a-int(a)!=0:
        print("El numero es negativo y real")
        
    if a==0:
        print("El numero es cero y entero")


def main():
    a=float(input("Ingrese un numero:"))
    b= analisis (a)


main()