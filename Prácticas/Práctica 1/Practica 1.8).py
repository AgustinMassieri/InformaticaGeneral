tiempo= int(input("Ingrese tiempo en segundos:"))

tiempod= tiempo//86400
tiempo1=tiempo-86400

tiempoh=tiempo1//3600
tiempo2=tiempo1-3600

tiempom=tiempo2//60
tiempo3= tiempo2-60

tiemps=tiempo3//1

print(tiempod,tiempoh,tiempom,tiempos)