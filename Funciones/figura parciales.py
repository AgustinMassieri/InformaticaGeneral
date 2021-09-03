##1
base=8
for f in range(base):
    for c in range(base):
        if f==0 or c==0 or f==base-1 or c==base-1 or (f>=4 and c<=3) or (f<=3 and c>=4):
            print("*",end="")
        else:
            print(" ",end="")
    print()

##2
base=10
for f in range (base):
    for c in range(base):
        if f==base-1 or c==base-1 or f==c or (f+c==base-1) or (f+c<=4):
            print("*",end="")
        else:
            print(" ",end="")
    print()
##3
base=9
for f in range(base):
    for c in range(base):
        if c==f or c==base//2 or (f+c==base-1) or (f==0 and c>=base//2) or (f==1 and (c==base-4 or c==base-3)) or (f==2 and c==base-4):
            print("*",end="")
        else:
            print(" ",end="")
    print()