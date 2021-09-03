def principioFin(texto):
    longitud=len(texto)
    letra1=texto[longitud-1]
    letra2=texto[0]
    if letra1==letra2:
        return True
    else:
        False
def main():
    texto=input("Ingrese un texto: ")
    principioFin(texto)
    if principioFin(texto)==True:
        print("El texto cumple la condición.")
    else:
        print("El texto no cumple la condición")
main()