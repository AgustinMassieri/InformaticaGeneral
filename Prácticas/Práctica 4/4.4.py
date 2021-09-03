def perfecto (contador):
    w=1
    sumador=0
    while w<contador:
        if (contador%w)==0:
            sumador=sumador+w
            w=w+1
        else:
            w=w+1
    if sumador==contador:
        return True
    else:
        return False

    
def main ():
    contador=0
    numperf=0
    while not numperf==4:
        if perfecto(contador)==True:
            print=contador
            contador=contador+1
            numperf=numperf+1
        else:
            contador=contador+1
        
main()