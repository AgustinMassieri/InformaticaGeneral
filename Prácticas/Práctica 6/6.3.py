def enLista (lista,num):
    return num in lista
def cargarLista (lista):
    num=1
    while num!=0:
        num=int(input("Ingrese numero:"))
        while enLista(lista,num):
            print("Error",end=" ")
            num=int(input("Ingrese numero:"))
        if num!=0:
            lista.append(num)
def carga(lista,lista2):
    print("CONJUNTO 1")
    cargarLista(lista)
    print("CONJUNTO 2")
    cargarLista(lista2)
    print(lista)
    print(lista2)
    print()
    
def union(lista,lista2):
    lista=lista+lista2
    print(lista)
    print()

def interseccion(lista,lista2):
    i=0
    interseccion=[]
    while i<len(lista):
        h=0
        while h<len(lista2):
            if lista[i]==lista2[h]:
                interseccion.append(lista[i])
            h+=1
        i+=1
    print(interseccion)
    print()

def diferencia(lista,lista2):
    i=0
    diferencia=lista
    while i<len(lista):
        h=0
        while h<len(lista2):
            if lista[i]==lista2[h]:
                diferencia.remove(lista[i])
            h+=1
        i+=1
    print(diferencia)
    print()
    
def diferenciaSimetrica (lista,lista2):
    cont1=0
    cont2=0
    listanueva=[]
    while cont1<len(lista):
        if not lista[cont1] in lista2:
            listanueva.append(lista[cont1])
        cont1+=1
    while cont2<len(lista2):
        if not lista2[cont2] in lista:
            listanueva.append(lista2[cont2])
        cont2+=1
    print(listanueva)
    print()
    
def main ():
    lista=[]
    lista2=[]
    num=1
    while num!=0:
        print("1. CARGAR CONJUNTO")
        print("2. UNION")
        print("3. INTERSECCION")
        print("4. DIFERENCIA (A-B)")
        print("5. DIFERENCIA SIMETRICA")
        print("0. SALIR")
        
        num=int(input("Ingrese el valor de la opcion:"))
    
        if num==1:
            carga(lista,lista2)
        if num==2:
            union(lista,lista2)
        if num==3:
            interseccion(lista,lista2)
        if num==4:
            diferencia(lista,lista2)
        if num==5:
            diferenciaSimetrica (lista,lista2)
        if num==0:
            print("Final del programa")
main()
