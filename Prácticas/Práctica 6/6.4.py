import random
def cargarListaAleat (n1,n2,cantidad):
    auxiliar=n1
    if n1>n2:
        n1=n2
        n2=auxiliar
    lista= [random.randint(n1,n2) for x in range(cantidad)]
    return lista

def minVal(lista):
    longitud=len(lista)
    n=max(lista)
    if lista==[]:
        return -1
    else:
        while longitud!=0:
            if lista[longitud-1]<n:
                n=lista[longitud-1]
            longitud-=1
        return n        


def maxVal(lista):
    longitud=len(lista)
    n=0
    if lista==[]:
        return -1
    else:
        while longitud!=0:
            if lista[longitud-1]>n:
                n=lista[longitud-1]
            longitud-=1
        return n       

    
def main():
    n1=int(input("Ingrese un número entero:"))
    n2=int(input("Ingrese un número entero:"))
    n3=int(input("Ingrese un número entero:"))
    cantidad=n3
    
    lista= cargarListaAleat(n1,n2,n3)
    print("Lista generada: ",lista)
    print()
    print("El valor máximo de la lista es: ",max(lista))
    print("El valor mínimo de la lista es: ",min(lista))
    print()
    print("El valor maximo de la lista por función es: ",maxVal(lista))
    print("El valor mínimo de la lista por función es: ",minVal(lista))
    
main()