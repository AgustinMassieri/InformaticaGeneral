import random
def main ():
    a1=input("Ingrese alternativa 1 para vestimenta:")
    a2=input("Ingrese alternativa 2 para vestimenta:")
    b1=input("Ingrese alternativa 1 para plato:")
    b2=input("Ingrese alternativa 2 para plato:")
    c1=input("Ingrese alternativa 1 para bebida:")
    c2=input("Ingrese alternativa 2 para bebida:")

    print("Cena al azar:",random.choice([a1,a2]) , random.choice([b1,b2]) , random.choice([c1,c2]))
main()