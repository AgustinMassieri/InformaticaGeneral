def main():
    a=int(input("Ingrese numeros enteros positivos (finalice con 0):"))
    mayor=a
    menor=a
    while a!=0:
        a=int(input(""))
        if mayor>=a:
            mayor=mayor
        elif mayor<=a:
            mayor=a
        if menor<=a and a!=0:
            menor=menor
        elif menor>=a and a!=0:
            menor=a
    print(mayor,menor)
            
main()

