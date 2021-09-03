def main():
    contadoraprobado=0
    contadoraplazo=0
    contadorpromo=0
    
    nota=int(input("Ingrese nota:"))

    if nota>=4 and nota<=7:
        contadoraprobado+=1
    elif nota<4 and nota>0:
        contadoraplazo+=1
    elif nota>7 and nota<=10:
        contadorpromo+=1
    
    while nota!=0:
        nota=int(input("Ingrese nota:"))
        if nota>=4 and nota<=7:
            contadoraprobado+=1
        elif nota<4 and nota>0:
            contadoraplazo+=1
        elif nota>7 and nota<=10:
            contadorpromo+=1
    
    print("")
    print("Cantidad de aplazos:{}".format(contadoraplazo))
    print("Cantidad de aprobados:{}".format(contadoraprobado))
    print("Cantidad de promocionados:{}".format(contadorpromo))
#print("Promedio general:{}".format())
main()