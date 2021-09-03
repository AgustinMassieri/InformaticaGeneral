def agregarMedia(nombreArch):
    lista=[]
    arch=open(nombreArch,"r")

    for renglon in arch:
        numero= renglon[:-1].split(";")
        lista.append(numero)
        
    arch.close()

    arch2=open(nombreArch,"w")

    for x in lista:
        promedio=0
        contador=0
        for y in x:
            arch2.write(str(y)+";")
            promedio = promedio + int(y)
            contador+=1
        arch2.write("\n")
        promedioTotal=promedio/contador
        
        arch2.write("Promedio total=" + str(promedioTotal)+"\n")

    arch2.close()
    
def main():
    agregarMedia("ej2.csv")
    
main()