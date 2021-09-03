def factura(ID_abonado):
    archivo = open("abonados.txt","r")

    pers = {}
    for renglon in archivo:
        persona = renglon[:-1].split(",")
        pers["ID_Abonado"] = int(persona[0])
        pers["Nombre"] = str(persona[1])
        pers["Domicilio"] = str(persona[2])
        pers["ID_Categoria"] = int(persona[3])

        if ID_abonado == pers["ID_Abonado"]:
            print("Nombre:",pers["Nombre"])
            print("Domicilio:",pers["Domicilio"])
                    
            archivo2 = open("categorias.txt","r")
            cat = {}
            for renglon2 in archivo2:
                categoria = renglon2[:-1].split(",")
                cat["ID_Categoria"] = int(categoria[0])
                cat["abonoTelefonico"] = float(categoria[1])
                cat["importeMinuto"] = float(categoria[2])
                
                if pers["ID_Categoria"] == cat["ID_Categoria"]:
                    print("Abono:",cat["abonoTelefonico"])
            
            
                    archivo3 = open("conexiones.txt","r")
                    conex = {}
                    suma=0
                    for renglon3 in archivo3:
                        conexion = renglon3[:-1].split(",")
                        conex["ID_Abonado"] = int(conexion[0])
                        conex["duracMinutos"] = int(conexion[1])
                        
                        if pers["ID_Abonado"] == conex["ID_Abonado"]:
                            suma=suma+conex["duracMinutos"]
                    print("Importe:", suma * cat["importeMinuto"])
                    print("Total:", (float(suma * cat["importeMinuto"]) + float(cat["abonoTelefonico"])))
                    
    archivo3.close()
    archivo2.close()
    archivo.close()
    
def duracionMaxima ():
    archivo3 = open("conexiones.txt","r")
    conex = {}
    lista=[]
    suma=0
    for renglon3 in archivo3:
        conexion = renglon3[:-1].split(",")
        lista.append(conexion)
    
    for i in range(1,len(lista)):
        for j in range (len(lista)-i):
            if (lista[j]>lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]

    memoria=0
    edades=[]
    listaImprimir=[]
    
    for dato in lista:
        
        if listaImprimir == [] and edades == []:
            memoria = dato[0]
            edades.append(dato[1])
            
        else:
            if memoria == dato[0]:
                edades.append(dato[1])
            else:
                listaImprimir.append([memoria,edades])
                memoria = dato[0]
                edades = []
                edades.append(dato[1])
                
    listaImprimir.append([memoria,edades])
    print(listaImprimir)
        

def main():
    ID_abonado = int(input("Ingrese el ID del abonado: "))
    
    factura(ID_abonado)
    duracionMaxima()
    
main()