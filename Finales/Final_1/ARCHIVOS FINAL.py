def ordenar ():



def calcularComision(ventatotal, Objetivo, Sueldoanual):
    
    if ventatotal < ((Objetivo*80)//100):
        comision=0
    
    elif ventatotal >= ((Objetivo*80)//100) and ventatotal < Objetivo:
        comision= ((Sueldoanual*3)//100)
    
    elif ventatotal >= Objetivo:
        comision= ((Sueldoanual*10)//100)
    
    return comision

def liquidar ():
    pers={}    
    arch=open("vendedores.csv","r")
    
    arch3=open("liquidacionComisiones.txt","w")

    
    for renglon in arch:
        persona= renglon[:-1].split(",")
        pers["Codigo"]= int(persona[0])
        pers["Nombre"]= persona[1]
        pers["Objetivo"]= int(persona[2])
        pers["Sueldoanual"]= float(persona[3])
        
        arch2=open("ventasTarjetas.csv","r")
        vent={}
        ventatotal=0
        for renglon2 in arch2:
            ventas= renglon[:-1].split(",")
            vent["Codigo"]= int(ventas[0])
            vent["mesVenta"]= ventas[1]
            vent["cantTarjeta"]= int(ventas[2])
            
            if vent["Codigo"] == pers["Codigo"]:
                ventatotal=ventatotal + vent["cantTarjeta"]
        
        arch2.close()        
        
        ventaVendedor= calcularComision(ventatotal,pers["Objetivo"],pers["Sueldoanual"])                
        
            
        arch3.write(str(pers["Codigo"]) + "," + str(ventaVendedor) + "\n")
        
        
    arch3.close()
    
    
def topCinco ():
    
    arch=open("vendedores.csv","r")
    arch1=open("liquidacionesComisiones.txt","r")
    
    per={}
    
    for renglon in arch:
        persona= renglon[:-1].split(",")
        per["Codigo"]= int(persona[0])
        per["Nombre"]= persona[1]
        
        vent={}        
        for renglon1 in arch1:
            venta=renglon[:-1].split(",")
            vent["Codigo"]=venta[0]
            vent["Comision"]=venta[1]
        
        if per["Codigo"] == vent["Codigo"]:
            

    
def main():
    liquidar()
        
    
    
    
main()