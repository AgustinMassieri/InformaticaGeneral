import math
def area_triangulo (base, altura):
    area= (base * altura) /2
    return area

def perimetro_triangulo (base, altura):
    perimetro= (base**2 + altura**2) + math.sqrt(base**2 + altura**2)
    return perimetro

def main():
    base= int(input("Ingrese base: "))
    altura= int(input("Ingrese altura: "))
    area= area_triangulo (base,altura)
    perimetro= perimetro_triangulo (base, altura)
    
    print("Calculos para un triangulo de base y altura ")
    print("<<< area= {:.2f} >>>     <<< perimetro= {:.2f}>>>".format(area, perimetro))
    
main()
