import math
def suma (a,b):
    resultado=a+b
    return resultado
    
def resta (a,b):
    resultado=a-b
    return resultado

def multi (a,b):
    resultado=a*b
    return resultado

def divi (a,b):
    resultado=a/b
    return resultado

def main():
    a=int(input("Ingrese el primer número:"))
    b=int(input("Ingrese el segundo número:"))
    oper=input("Ingrese la operacion (+, -, *, /):")
    if oper=="+":
        resultado= suma(a,b)
        print(resultado)
    if oper=="-":
        resultado= resta(a,b)
        print (resultado)
    if oper=="*":
        resultado= multi (a,b)
        print (resultado)
    if oper=="/":
        resultado= divi (a,b)
        print(resultado)
main()