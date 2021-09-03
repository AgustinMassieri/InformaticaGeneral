def esletra(l):
    return (l>='a' and l<='z') or (l>='A' and l<='Z') or l in 'áÁéÉíÍóÓuÚñÑ'

def procesar(texto):
    listaPalabras=[]
    i=0
    while i<len(texto):
        while i<len(texto) and not esletra(texto[i]):
            i+=1
        comienzo=i
        while i < len(texto) and (esletra(texto[i])):
            i += 1
        final=i-1
        palabra=texto[comienzo:final + 1]
        existe=False
        for x in listaPalabras:
            if x[0]== palabra:
                x[1]=int(x[1])+1
                existe=True
        if existe!=True:
            listaPal=[palabra,1]
            listaPalabras.append(listaPal)
        
    return listaPalabras

def frecuenciaPalabra (nombreArchivo):
    arch=open(nombreArchivo,"r")
    texto=arch.readline()
    list=procesar(texto)
    
    arch.close()

    arch2=open("frecuencias.csv","w")

    for h in list:
        pal=h
        arch2.write(pal[0]+", "+ str(pal[1])+"\n")
    
    
def main():
    frecuenciaPalabra("hola.txt")
        
main()