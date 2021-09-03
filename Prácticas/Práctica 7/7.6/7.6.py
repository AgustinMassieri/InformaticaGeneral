import random
def generadora (ori,dest,cant):
    archivo=open(ori,"r")
    archivo2=open("destino.txt","w")
    lista=[]
    lista2=[]
    
    for renglon in archivo:
        numero= renglon [:-1]
        lista.append(numero)

    contador=0
    while contador<cant:
        a=random.randrange(1,len(lista))
        if lista[a] not in lista2:
            lista2.append(lista[a])
            archivo2.write(lista[a] + "\n")
            contador+=1
        
    archivo.close()
    archivo2.close()
    
def main():
    cant=5
    ori="origen.txt"
    dest = "destino.txt"
    generadora (ori,dest,cant)
    
main()