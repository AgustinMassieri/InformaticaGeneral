def ordenar(texto):
    cantmitad=len(texto)//2
    a=""
    for i in range(cantmitad):
        a=a+texto[i]

    b=""
    while not cantmitad==len(texto):
        b=b+texto[cantmitad]
        cantmitad+=1
    print(b+a)
def main():
    texto=input("Ingrese un texto: ")
    ordenar(texto)
main()