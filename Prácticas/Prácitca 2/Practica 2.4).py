import math
def areac(diaC):
    radio= diaC/2
    areaCir= math.pi*(radio**2)
    return areaCir

def areaC(numero):
    areaCua=numero**2
    return areaCua

def arean(areaC1,areaC2,areaC3,areaCua):
    areaN= areaCua- areaC1 - (areaC2)*2
    return areaN

def main ():
    numero= int(input("Ingrese el lado: "))
    d1= int(input("Ingrese diametro 1: "))
    d2= int(input("Ingrese diametro 2: "))
    d3= int(input("Ingrese diametro 3: "))

    areaC1= areac (d1)
    areaC2= areac (d2)
    areaC3= areac (d3)

    areaCua= areaC (numero)
    areanegra= arean(areaC1,areaC2,areaC3,areac)
    print("El area negra es",areanegra)

main()