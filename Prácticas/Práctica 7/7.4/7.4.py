def esletra(l):
    return (l>='a' and l<='z') or (l>='A' and l<='Z') or l in 'áÁéÉíÍóÓuÚñÑ'


def cabecera (arch,cant,pmin,pmax):
    archivo=open(arch,"r")
    texto=archivo.readline()
    
    i=0
    contador=0
    
    while i<len(texto) and contador<cant:
        while i<len(texto) and not esletra(texto[i]):
            i+=1
        comienzo=i
        while i < len(texto) and (esletra(texto[i])):
            i += 1
        final=i-1
        palabra=texto[comienzo:final + 1]
        if len(palabra)<=pmax and len(palabra)>=pmin:
            print(palabra)
            contador+=1
            
    archivo.close()
    
    
def main():
    arch="hola.txt"
    cant=5
    pmin=5
    pmax=1
    cabecera (arch,cant,pmin,pmax)    
    
main()