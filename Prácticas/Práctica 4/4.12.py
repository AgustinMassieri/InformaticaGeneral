def dibujo(base,altura):
    for x in range(altura):
        for y in range(base):
            if y==0 or (y==base and x==base) or (x==base-1 and y==base-1) or (x==base-1 and y==base-2) or (x==base-1 and y==base-3) or (x==base-1 and y==base-4) or (x==base-2 and y==base-4) or (x==base-2 and y==base-3)or (x==base-2 and y==base-2)or (x==base-3 and y==base-3) or (x==base-3 and y==base-4) or (x==base-4 and y==base-4):
                print("*",end="")
            else:
                print(" ",end="")
        print()

def main():
    base=int(input("Ingrese base: "))
    while base<3:
        print("Error, debe ser mayor o igual a 3")
        base=int(input("Ingrese base: "))
    altura=base
    dibujo(base,altura)
main()