def main ():
    a=int(input("Ingrese un numero A:"))
    b=int(input("Ingrese un numero B:"))
    if a>b:
        resta=a-b 
        if resta>=b and resta<=a :
            print("SI cumple la condicion.")
        else:
            print("NO cumple la condicion.")
    else:
        resta=b-a
        if resta>=a and resta<=b:
            print("SI cumple la condicion.")
        else:
            print("NO cumple la condicion.")
    
main ()