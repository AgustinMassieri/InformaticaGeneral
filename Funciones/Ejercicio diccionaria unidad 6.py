def agregar(capitales):
    pais=input("Ingrese el nombre del país: ")
    ciudad=input("Ingrese el nombre de la ciudad: ")
    capitales[pais] =ciudad
    
def borrar(capitales):
    borrar=input("Ingrese el país a eliminar: ")
    if borrar in capitales.keys():
        del capitales[borrar]
    else:
        if borrar not in capitales.values():
            print("No se encontro dicho país o ciudad.")
        else:
            for indice in capital.copy().keys():
                if capitales[indice]== borrar:
                    del capitales[indice]
                    
def buscar(capitales):
    print(capitales.get(input("Ingrese el país: ")))

def vaciar(capitales):
    for indice in capitales.copy():
        del capitales[indice]

def mostrar(capitales):
    for pais in capitales:
        print(pais,"--->",capitales[pais])
        
def opcionMenu():
    print("1-Agregar")
    print("2-Borrar")
    print("3-Buscar")
    print("4-Vaciar")
    print("5-Mostrar")
    print("6-Salir")
    
    opc=int(input("Ingrese su opción: "))
    while not (opc>=1 and opc<=6):
        print("Error. Opción inválida")
        opc=int(input("Ingrese su opción: "))
    return opc
def main():
    capitales = dict()
    
    opc=opcionMenu()
    while opc !=6:
        if opc==1:
            agregar(capitales)
        elif opc==2:
            borrar(capitales)
        elif opc==3:
            buscar(capitales)
        elif opc==4:
            vaciar(capitales)
        elif opc==5:
            mostrar(capitales)
        
        opc=opcionMenu()
    
main()