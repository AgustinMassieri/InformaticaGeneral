def bono (sueldobase):
    if sueldobase > 2000:
        bono= (15*sueldobase)//100
    else:
        bono= (20*sueldobase)//100
    return bono

def plusC (sueldobase,hijos):
    if hijos=="s":
        plushijos= (5*sueldobase)//100
    return plushijos

def plusH (sueldobase,hijos,categoria):
    if categoria==4 or categoria==5 or categoria==6 or categoria==1 or categoria==2 or categoria==3:
        plushijos= plusC(sueldobase,hijos)
    return plushijos    

def abc (sueldobase,categoria):
    if categoria==7 or categoria==8 or categoria==9:
        sueldofinal= sueldobase +  ((20*sueldobase)//100) + bono(sueldobase)
   
    if categoria==4 or categoria==5 or categoria==6:
        sueldofinal= sueldobase + ((12*sueldobase)//100) + bono(sueldobase)
        
    if categoria==1 or categoria==2 or categoria==3:
        sueldofinal= sueldobase + ((10*sueldobase)//100) + bono(sueldobase)

    return sueldofinal
        
def main():
    sueldobase=int(input("Ingrese el sueldo base:"))
    hijos=str(input("Tiene hijos? (s/n):"))
    categoria=int(input("Ingrese categoria (1-9): "))
    sueldo= abc(sueldobase,categoria) + plusH(sueldobase,hijos,categoria)
    print("El sueldo total será de ${:.2f}".format(sueldo))
main()