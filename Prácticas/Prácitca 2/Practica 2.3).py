def main():
    numero= int(input("Ingrese un numero binario de hasta 8 bits: "))

    n1= numero%10
    numero= numero//10

    n2= numero%10
    numero= numero//10

    n3= numero%10
    numero= numero//10

    n4= numero%10
    numero= numero//10
    
    n5= numero%10
    numero= numero//10

    n6= numero%10
    numero= numero//10

    n7= numero%10
    numero= numero//10

    n8= numero%10
    numero= numero//10

    bit= n1+n2+n3+n4+n5+n6+n7+n8
    r= bit%2
    print("Bit de paridad generado:",r)

main()