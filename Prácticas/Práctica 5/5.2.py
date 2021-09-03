def funcion(palabra,extremos,extremo1,extremo2):
    cantidad=len(extremos)
    if cantidad<2:
        print("")
        print("La función ha retornado una palabra vacia.")
    else:
        print("")
        print("La función retornó:",extremo1+palabra+extremo2)

def main():
    extremos=input("Ingrese los extremos: ")
    palabra=input("Ingrese una palabra: ")
    extremo1=extremos[0]
    extremo2=extremos[1]
    funcion(palabra,extremos,extremo1,extremo2)
main()