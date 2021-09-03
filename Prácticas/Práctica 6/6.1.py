def estaEnLista1 (num,lst1):
    if num in lst1:
        return True
    else:
        return False

def estaEnLista2 (num,lst1):
    for i in range (len(lst1)):
        if lst1[i]==num:
            return True
    return False
    
def estaEnLista3 (num,lst1):
    contador=0
    while contador<len(lst1):
        if lst1[contador]==num:
            return True
        contador+=1
    return True
def main():
    num=23
    lst=[1,2,3,4]
    lst1=[1,23,3,4]
    lst2=[]
    estaEnLista1(num,lst1)
    estaEnLista2(num,lst1)
    estaEnLista3(num,lst1)
main()