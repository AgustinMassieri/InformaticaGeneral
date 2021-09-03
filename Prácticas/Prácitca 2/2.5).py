import random

def main ():
    l1=int(input("Ingrese el limite superior (numero natural):"))
    l2=int(input("Ingrese el limite inferior (numero natural):"))
    
    num=(random.randint(l2,l1))
    num2=(random.randint(l2,num))
    num3=(random.randint(l2,num2))
    
    print("Limite inferior {}, limite superior {}. Numero generado: {}".format(l2,l1,num))
    print("Limite inferior {}, limite superior {}. Numero generado: {}".format(l2,num,num2))
    print("Limite inferior {}, limite superior {}. Numero generado: {}".format(l2,num2,num3))
    
main()
    
    

