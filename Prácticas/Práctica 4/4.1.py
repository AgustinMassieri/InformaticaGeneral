def main():
    cont=0
    cantidad=4

    a=int(input("Ingrese un número entero: "))
    if a%2==0 and a// 4==0:
        print("Numero par. Tambien es multiplo de 4")
    elif a%2==0:
        print("Numero par")

    while cont<cantidad:
        if a%2 ==0:
            cont+=1
        a=int(input("Ingrese un número entero: "))
        if a%2==0 and a%4==0:
            print("Numero par. Tambien es multiplo de 4. Total de numeros pares ingresados:{}".format(cont+1))
        elif a%2==0:
            print("Numero par. Total de numeros pares ingresados:{}".format (cont+1))
    print("")
    print("FIN")
main()