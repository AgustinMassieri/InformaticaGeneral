def esLetra(h):
    if "a"<=h<="z" or "A"<=h<="Z":
        return True
    else:
        return False
def esMinuscula(h):
    if "A"<=h<="Z":
        return chr(ord(h)+32)
    else:
        return h
def limpiar(frase):
    l=0
    frase2=""
    while l<len(frase):
        while l<len(frase) and not esLetra(frase[l]):
            l+=1
        while l<len(frase) and esLetra(frase[l]):
            frase2=frase2+frase[l]
            l+=1
    return frase2
def main():
    frase="Asi Ramona va, no Marisa"
    frase2=limpiar(frase)
    longitud=len(frase2)
    j=""
    k=""
    for i in range(longitud):   
        h=j+frase2[i]
        k=k+esMinuscula(h)
    vuelta=k[::-1]
    if vuelta==k:
        print("La frase es palíndroma!")
    else:
        print("La frase no es palíndroma!")

main()