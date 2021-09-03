def crearRectangulo (ancho,alto):
    rectangulo= (crearFila(a)+"/n")*alto
    return rectangulo

def crearFila (ancho):
    linea="*" *a
    return linea

def main ():
    a=5
    ancho= int(input("Ingrese ancho: "))
    alto= int(input("Ingrese alto: "))
    print(crearRectangulo(ancho,alto))
    
main()