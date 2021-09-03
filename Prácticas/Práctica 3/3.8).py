def prom (n1,n2,n3):
    promedio= (n1+n2+n3)/3
    return promedio

def promg (n1,n2,n3,n4):
    promediogeneral= (n1+n2+n3+n4)/4
    return promediogeneral
    
def main ():
    n1=int(input("Ingrese la nota del primer parcial:"))
    n2=int(input("Ingrese la nota del segundo parcial:"))
    n3=int(input("Ingrese la nota del tercer parcial:"))
    promedio= prom(n1,n2,n3)
    
    
    if n1>=4 and n2>=4 and n3>=4 and ((n1+n2+n3)/3) >7:
        print("El alumno promociona la materia con la nota {:.2f}".format(promedio))
    if n1>=4 and n2>=4 and n3>=4 and ((n1+n2+n3)/3) <7:
        print("El alumno deberá rendir final.")

    if n1<4 or n2<4 or n3<4:
        n4=int(input("Ingrese la nota del recuperatorio:"))
        if n4 >= 4:
            print("Promedio General= {:.1f}".format(promg(n1,n2,n3,n4)))
            print("Aprobado")
        else:
            print("Aplazado")

main()