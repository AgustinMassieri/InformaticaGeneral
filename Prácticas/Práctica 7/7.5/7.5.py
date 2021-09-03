def esMinuscula(l):
    if "A"<=l<="Z":
        return chr(ord(l)+32)
    else:
        return l

def esletra(l):
    return (l>='a' and l<='z') or (l>='A' and l<='Z') or l in 'áÁéÉíÍóÓuÚñÑ'


def cabecera2 (arch,cant,pmin,pmax):
    archivo=open(arch,"r")
    archivo2=open("resultado.csv","w")
    texto=archivo.readline()
    lista=[]
    
    
    i=0
    contador=0
    
    while i<len(texto) and contador<cant:
        while i<len(texto) and not esletra(texto[i]):
            i+=1
        comienzo=i
        palabra = ''
        while i < len(texto) and (esletra(texto[i])):
            
            if esletra(texto[i]):
                palabra = palabra + esMinuscula(texto[i])
            i += 1
        final=i-1
        
        if len(palabra)<=pmax and len(palabra)>=pmin and not (palabra in lista):
            lista.append(palabra)
            contador+=1
            
            archivo2.write(palabra + "\n")
    archivo.close()
    print(lista)
    archivo2.close
    
def main():
    arch="hola.txt"
    cant=14
    pmin=3
    pmax=9
    cabecera2 (arch,cant,pmin,pmax)    
    
main()