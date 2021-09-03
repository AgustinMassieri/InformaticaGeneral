def esletra(l):
    return (l>='a' and l<='z') or (l>='A' and l<='Z') or l in 'áÁéÉíÍóÓuÚñÑ'

def contpalabra(texto, pal):
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
            if pal == (texto[comienzo:final + 1]):
                cont+=1

    return print(cont)


def main():
    texto=input('ingrese el texto:')
    palabra=input('Ingrese una frase para encontrar dentro del texto: ')
    contpalabra(texto,palabra)

main()