numero=int(input("Ingrese número:"))

dig1= numero %10
numero= numero/10


dig2= numero %10
numero= numero / 10


dig3= numero %10
numero= numero / 10


dig4= numero %10
numero= numero / 10


dig5= numero %10



print("Separación en digitos:", int(dig5)**2, "-", int(dig4)**2, "-", int(dig3)**2, "-", int(dig2)**2, "-", int(dig1)**2)