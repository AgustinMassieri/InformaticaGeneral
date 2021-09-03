def cantHabitantes(nombreLocalidad,hijos):
    archivo = open("localidades.txt","r")
    archivo2 = open("habitantesXlocalidad.txt","r")
    archivo3 = open("habitantes.txt","r")
    
    for renglon in archivo:
        localidad = renglon[:-1].split(",")
        if localidad[1] == nombreLocalidad:
            ciudad = localidad
    lista=[]
    for renglon2 in archivo2:
        habs = renglon2[:-1].split(",")
        if habs[0] == ciudad [0]:
            lista.append(habs[1])
    
    listaFinal=[]
    
    for renglon3 in archivo3:
        pers = renglon3[:-1].split(",")
        if (pers[0] in lista) and (hijos == int(pers[2])) :
            h = str(pers[0]) + " , " + str(pers[1])
            listaFinal.append(h)
    
    print(listaFinal)
            
    
def edadXlocalidad ():
    archivo = open("habitantesXlocalidad.txt","r")
    localidades = []
    idLocalidades = []
    for renglon in archivo:
        localidad = renglon[:-1].split(",")
        localidades.append(localidad)
        idLocalidades.append(localidad[0])
    archivo.close()
    
    archivo = open("habitantes.txt","r")
    habitantes=[]
    
    for renglon in archivo:
        habitante = renglon[:-1].split(",")
        habitantes.append(habitante)
    archivo.close()
    
    listaFinal=[]
    for sl1 in localidades:
        
        for sl2 in habitantes:
            
            if sl1[1] == sl2[0]:
                lista=[sl1[0],sl2[3]]
                listaFinal.append(lista)

    for i in range(1,len(listaFinal)):
        for j in range (len(listaFinal)-i):
            if (listaFinal[j]>listaFinal[j+1]):
                listaFinal[j], listaFinal[j+1] = listaFinal[j+1], listaFinal[j]
    
    print(listaFinal,"\n")
    memoria=0
    edades=[]
    listaImprimir=[]
    
    for dato in listaFinal:
        
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
        
def main ():
    nombreLocalidad="Adolfo Alsina"
    hijos=1
    cantHabitantes(nombreLocalidad,hijos)
    edadXlocalidad()   
    
main()