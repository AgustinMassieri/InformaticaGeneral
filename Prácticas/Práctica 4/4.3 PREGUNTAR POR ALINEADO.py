def primo (numero):
    if numero <2:
        return False
    for i in range(2,numero):
        if numero%i ==0:
            return False
    return True

def main ():
    numero=int(input("Ingrese  cantidad (numero natrual):"))
    for numero in  range (1,numero+1):
        if primo(numero):
            print(numero)
    
    generador=0
    numencontrado=0
    
    while not numencontrado==57:
        if primo(generador):
            print(generador)
            generador= generador +1
            numencontrado= numencontrado +1
        else:
            generador= generador+1
            
"""    contador=0
    while contador<numero:
        if primo(numero):
            contador+=1
            print(numero)
    
   """ 
main()