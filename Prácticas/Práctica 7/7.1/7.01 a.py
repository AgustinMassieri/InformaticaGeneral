def funcion (nombreArch):
    lista=[]
    arch=open(nombreArch,"r")
    total=0
    promedio=0
    primerIngreso=True
    
    for renglon in arch:
        numero= renglon[:-1]
        if primerIngreso:
            mayor=numero
            menor=numero
            primerIngreso=False
        total+=1
        promedio=promedio+int(numero)
        if numero>mayor:
            mayor=numero
        elif numero<menor:
            menor=numero
    
    promediototal=promedio//total
    lista.append(mayor)
    lista.append(menor)
    lista.append(total)
    lista.append(promediototal)
    arch.close()
    
    return lista

def main():
    
    print(funcion("informe.txt"))
    
main()