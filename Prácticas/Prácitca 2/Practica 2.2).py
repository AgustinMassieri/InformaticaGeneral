import math
def raiz (b,e):
    resultado= math.pow(b,1/e)
    return resultado

def main():
    b= int(input("Ingrese el radicando (numero real): "))
    e= int(input("Ingrese el indice (numero natural): "))
    r= raiz(b,e)
    print("La raiz {0} de {1} es: {2}".format (b,e,r))
main()
