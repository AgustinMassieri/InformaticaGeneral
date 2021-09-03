def multa (velocvehiculo,velocmaxpermitida,tipodevehiculo):
    if (velocmaxpermitida*15)//200<velocvehiculo<velocmaxpermitida+((velocmaxpermitida*15)//100):
        mensaje= "No recibe multa."
    else:
        if velocvehiculo<(velocmaxpermitida*15)//100 and tipodevehiculo=="n" :
            mensaje= "Advertencia."
        else:
            mensaje= "No recibe multa."
    
        if (velocmaxpermitida*15)//200<velocvehiculo:
            mensaje= "Advertencia."

        if velocvehiculo > (velocmaxpermitida*15)//100 and tipodevehiculo=="n" :
            mensaje= "Recibe multa por exceso de velocidad."
        else:
            mensaje= "No recibe multa."
        
        if (velocmaxpermitida*15)//200 > velocvehiculo:
            mensaje= "Recibe multa por entorpecer el tránsito"
    
    return mensaje

def main():
    velocvehiculo= int(input("Velocidad del vehículo: "))
    velocmaxpermitida= int(input("Velocidad máxima: "))
    tipodevehiculo= str(input("Emergencia (s/n): "))
    velocminima= velocmaxpermitida/2
    print(multa(velocvehiculo,velocmaxpermitida,tipodevehiculo))
main()