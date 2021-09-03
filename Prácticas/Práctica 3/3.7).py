def par (a,b,c):
    if a>=b and a>c and b>c:
        resultado=(a+c)/2
        if resultado==b:
            d=True
        else:
            d=False
    if b>a and b>c and a>c:
        resultado=(b+c)/2
        if resultado==a:
            d=True
        else:
            d=False
    if c>a and c>b and b>a:
        resultado=(c+a)/2
        if resultado==b:
            d=True
        else:
            d=False
    if a>b and c>b and a>c:
        resultado=(a+b)/2
        if resultado==c:
            d=True
        else:
            d=False
    if b>a and b>c and c>a:
        resultado=(b+a)/2
        if resultado==c:
            d=True
        else:
            d=False
    if c>a and c>b and a>b:
        resultado=(c+b)/2
        if resultado==a:
            d=True
        else:
            d=False
    return d
def main ():
    a=int(input("Ingrese el primer numero:"))
    b=int(input("Ingrese el segundo numero:"))
    c=int(input("Ingrese el tercer numero:"))
    d= par (a,b,c)
    if d:
        print("Estan igualmente distanciados!")
    else:
        print("NO estan igualmente distanciados!")
main()