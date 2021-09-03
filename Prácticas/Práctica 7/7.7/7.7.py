listadni = []
def cargarLista ():
    archivo= open("persona.csv","r")
    for renglon in archivo:
            persona = renglon[:-1].split(",")
            listadni.append(persona[2])
    archivo.close()
    
def agregarRegistro ():
    archivo = open("persona.csv","a")
    
    nombre = str(input("Ingrese nombre: "))
    apellido = str(input("Ingrese apellido: "))
    dni = str(input("Ingrese D.N.I: "))
    while dni in listadni:
        dni = str(input("Error. Ingrese un D.N.I valido: "))
    listadni.append(dni)
    
    
    archivo.write(nombre + "," + apellido + "," + dni + "\n")
    
    archivo.close()

def eliminar ():
    lista1=[]
    dni = str(input("Ingrese D.N.I: "))
    while dni not in listadni:
        dni = str(input("Error. Ingrese D.N.I: "))
        
    archivo = open("persona.csv","r")
    
    
    condicion=False
    for renglon in archivo:
            persona = renglon[:-1].split(",")
            
            if  persona[2] == dni:
                condicion = True
            else:
                lista1.append(persona)        
                
    if condicion==False:
        print("No se encontraron resultados")
    
    archivo.close()
    
    archivo= open("persona.csv","w")
    
    for x in lista1:
        archivo.write(str(x[0])+","+str(x[1])+","+str(x[2])+"\n")     
    archivo.close()
    
def buscar ():
    archivo = open("persona.csv","r")
    
    print("1. BUSCAR POR D.N.I")
    print("2. BUSCAR POR APELLIDO")
    pregunta = int(input("Ingrese su opcion: "))
    
    if pregunta == 1:
        dni = str(input("Ingrese su D.N.I: "))
        
        condicion=False
        
        for renglon in archivo:
                persona = renglon[:-1].split(",")
                
                if  persona[2] == dni:
                    condicion = True
                    print(persona[0]+"," + persona[1] + "," + persona[2])
                    
        if condicion==False:
            print("No se encontraron resultados")
            
        
    elif pregunta == 2:
        apellido = str(input("Ingrese su apellido: "))
        condicion2 = False
        
        for renglon in archivo:
                persona = renglon[:-1].split(",")
                
                if  persona[2] == apellido:
                    condicion2 = True
                    print(persona)
                    
        if condicion2==False:
            print("No se encontraron resultados")
    
    archivo.close()
"""    
def ordenar ():
    print(1. ORDENAR POR NOMBRE)
    print(2. ORDENAR POR APELLIDO)
    print(3. ORDENAR POR D.N.I)
    
    eligir=int(input("Ingrese su eleccion: "))
    
    if elegir == 1:
        
    elif elegir == 2:
        
        
    elif elegir == 3:
"""    

def mostrar ():
    
    archivo = open("persona.csv","r")
    
    for renglon in archivo:
        persona = renglon[:-1]
        print(persona)
    
    archivo.close()
    
def main ():
    cargarLista()
    print()
    print("1. AGREGAR REGISTRO")
    print("2. ELIMINAR REGISTRO")
    print("3. BUSCAR REGISTRO")
    print("4. ORDENAR ARCHIVO POR")
    print("5. MOSTRAR ARCHIVO")
    print("6. SALIR")
    print()
    opcion = int(input("Ingrese el valor de la opcion: "))
    print()
    
    while opcion != 6:
        if opcion == 1:
            agregarRegistro()
        elif opcion == 2:
            eliminar()
        elif opcion == 3:
            buscar()
##        elif opcion == 4:
##            ordenar()
            
        elif opcion == 5:
            mostrar()
        
        print()
        print("1. AGREGAR REGISTRO")
        print("2. ELIMINAR REGISTRO")
        print("3. BUSCAR REGISTRO")
        print("4. ORDENAR ARCHIVO POR")
        print("5. MOSTRAR ARCHIVO")
        print("6. SALIR")
        print()
        opcion = int(input("Ingrese el valor de la opcion: "))
        print()
    
    if opcion == 6:
        print("FIN")
main()