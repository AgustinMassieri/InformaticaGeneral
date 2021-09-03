def funcion(palabra):
    cantidad=len(palabra)
    if cantidad<2:
        print("La función ha retornado una palabra vacia.")
    else:
        l1=palabra[cantidad-1]
        l2=palabra[cantidad-2]
        print("La función ha retornado: ",l2+l1+l2+l1+l2+l1)   

def main():
    palabra=input("Ingrese una palabra: ")
    funcion(palabra)
main()