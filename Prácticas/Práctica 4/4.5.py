def condicion (num):
    mil=num//1000
    num=num%1000

    centena=num//100
    num=num%100

    decena=num//10
    num=num%10

    unidad=num

    if unidad+centena== mil+decena:
        return True
    else:
        return False

def main():
    for v in range(1000,10000):
        if condicion(v):
            print(v)
main()