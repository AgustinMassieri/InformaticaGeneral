def esletra(l):
    return (l>='a' and l<='z') or (l>='A' and l<='Z') or l in 'áÁéÉíÍóÓuÚñÑ'

def modificar(palabra, pos, letra):
    return palabra[:pos]+ letra + palabra[pos+1:]
def aMayuscula(l):
    if l>='a' and l<= 'z':
        return chr(ord(l) - (ord('a') - ord('A')))
    else:
        return l
def procemodi(texto):
    i = 0
    while i < len(texto):
        while i < len(texto) and not (esletra(texto[i])):
            i += 1

        comienzo = i
        while i < len(texto) and (esletra(texto[i])):
            i += 1
        final = i - 1
        if comienzo <= final:
            texto=modificar(texto, comienzo, aMayuscula(texto[comienzo]))


    return texto


def main():
    texto = input('ingrese la palabra a modificar y convertir primeras letras en mayus: ')
    print(procemodi(texto))

main()