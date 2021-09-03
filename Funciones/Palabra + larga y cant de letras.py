def esletra(l):
    return (l>='a' and l<='z') or (l>='A' and l<='Z') or l in 'áÁéÉíÍóÓuÚñÑ'

def palmasletras(texto):
    i=0
    contle=0
    max=0
    while i < len(texto):
        while i < len(texto) and not (esletra(texto[i])):
            i += 1
        comienzo=i
        contle=0
        while i < len(texto) and (esletra(texto[i])):
            i += 1
            contle+=1
        final=i-1
        if comienzo<=final:
         if contle>max:
             max=contle
             cmaxi=comienzo
             fmaxi=final

    print(texto[cmaxi:fmaxi+1])
    return print(contle)


def main():
    texto=input('ingrese el texto para saber cual y cuantas letras tiene la palabra mas larga: ')
    palmasletras(texto)

main()