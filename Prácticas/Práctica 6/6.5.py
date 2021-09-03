import random
def cargarListaAleat ():
    n1=1
    n2=100
    cantidad=5
    lista= [random.randint(n1,n2) for x in range(cantidad)]
    return lista


def cambiaLista(lista,a,b):
    cantidad=5
    lista2= [random.randint(a,b) for y in range(cantidad)]
    return lista2
    
def main():
    lista=cargarListaAleat()
    print("Lista generada: ",lista)
    print()
    a=int(input("Ingrese limite a del rango:")) 
    b=int(input("Ingrese limite b del rango:"))
    print()
    lista2=cambiaLista(lista,a,b)
    print("Lista modificada: ",lista2)
main()
