def dibujo(base,altura):
    for x in range(altura):
        for y in range(base):
            if x==0 or x==altura-1 or y==0 or y==base-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
def main():
    base=int(input("Ingrese base: "))
    while base<2:
        print("Error, debe ser mayor o igual a 2")
        base=int(input("Ingrese base: "))
    
    altura= int(input("Ingrese altura: "))
    while altura<2:
        print("Error, debe ser mayor o igual a 2")
        altura=int(input("Ingrese altura: "))
    dibujo(base,altura)
main()