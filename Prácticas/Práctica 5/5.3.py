def primeraMitad(palabra):
    cantmitad=len(palabra)//2
    a=""
    for i in range(cantmitad):
        a=a+palabra[i]
    print("La función ha retornado: ",a)
def main():
    palabra=input("Ingrese una palabra de longitud par: ")
    primeraMitad(palabra)
main()