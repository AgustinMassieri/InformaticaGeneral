def esletra(l):
    return (l>='a' and l<='z') or (l>='A' and l<='Z') or l in 'áÁéÉíÍóÓuÚñÑ'
def procesar(texto):
    i=0
    palmax=""
    palmin=texto
    contpal=0
    while i < len(texto):
        while i < len(texto) and not (esletra(texto[i])):
            i += 1
        comienzo=i
        while i < len(texto) and (esletra(texto[i])):
            i += 1
        final=i-1
        if len(texto[comienzo:final+1])>len(palmax):
            palmax=texto[comienzo:final+1]
        if len(texto[comienzo:final+1])<len(palmin):
            palmin=texto[comienzo:final+1]
        contpal +=1
    return print(" Palabra de mayor longitud: {}\n Palabra de menor longitud: {}\n Su texto tiene {} palabras".format(palmax,palmin,contpal))

def main():
    pal=input("ingrese texto: ")
    procesar(pal)
main()