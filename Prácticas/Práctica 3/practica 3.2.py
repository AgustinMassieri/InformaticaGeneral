def ordenar (a,b,c):
    if a<b and b<c:
        a=a
        b=b
        c=c
        resultado= a,b,c
        return resultado
        
    if b<a and c<a and b<c:
        a=a
        b=b
        c=c
        resultado= b,c,a
        return resultado
    
    if a<b and b>c:
        a=a
        b=b
        c=c
        resultado= a,c,b
        return resultado

    if a<c and b<a:
        a=a
        b=b
        c=c
        resultado= b,c,a
        return resultado

    if c<b and b<a:
        a=a
        b=b
        c=c
        resultado= c,b,a
        return resultado
    
def main():
    a=int(input("Ingrese el primer número:"))
    b=int(input("Ingrese el segundo número:"))
    c=int(input("Ingrese el tercer número:"))
    d= ordenar (a,b,c)
    print (d)

main()