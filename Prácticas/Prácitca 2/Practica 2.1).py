import math
def areaTriangulo (p,L1,L2,L3):
    resultado= math.sqrt(p*(p-L1)*(p-L2)*(p-L3))
    return resultado

def main():
    L1= int(input("Ingrese lado 1: "))
    L2= int(input("Ingrese lado 2: "))
    L3= int(input("Ingrese lado 3: "))
    p= (L1+L2+L3)/2
    r= areaTriangulo(p,L1,L2,L3)
    print("El area del triangulo es ={:.2f}".format(r))
main ()