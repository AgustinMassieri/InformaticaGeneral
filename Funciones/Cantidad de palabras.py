def esletra(l):
    return (l>='a' and l<='z') or (l>='A' and l<='Z') or l in 'áÁéÉíÍóÓuÚñÑ'

def cantpalabra(texto):
    i=0
    cont=0
    while i < len(texto):
        while i < len(texto) and not (esletra(texto[i])):
            i += 1
        comienzo=i
        while i < len(texto) and (esletra(texto[i])):
            i += 1
        final=i-1
        if comienzo<=final:
           cont+=1

    return print(cont)


def main():
    texto=input('ingrese el texto para saber cuantas palabras tiene: ')
    cantpalabra(texto)

main()