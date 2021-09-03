def main():
    numdecimal=int(input("Ingrese un numero decimal (maximo 5 cifras):"))
    
    num1=numdecimal //8
    nu1=numdecimal-num1*8
    
    num2=num1 //8
    nu2=num1-num2*8
    
    num3=num2 //8
    nu3=num2 - num3*8
    
    num4=num3 //8
    nu4= num3 -num4*8
    
    print("Numero en octal: ",nu1,nu2,nu3,nu4)


main()