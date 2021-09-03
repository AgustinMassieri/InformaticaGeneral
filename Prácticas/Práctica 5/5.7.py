def larincort(corta,larga):
    dist=len(corta)
    cont=0
    x=0
    y=dist
    while y <= len(larga):
        if corta in larga[x:y]:
            cont+=1

        x+=1
        y+=1
    return cont

def main():
    larga=input("Ingrese una frase larga: ")
    corta=input("Ingrese una frase corta: ")
    print("La frase corta se encuentra",larincort(corta,larga),"veces en la larga")

main()