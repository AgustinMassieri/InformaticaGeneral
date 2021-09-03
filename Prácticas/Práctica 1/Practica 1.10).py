numbinario= int(input("Ingrese numero binario: "))

num1= numbinario %10
dec1= num1**1
numbinario= numbinario//10

num2= numbinario %10
dec2= num2**2
numbinario= numbinario//10


num3= numbinario %10
dec3= num3**3
numbinario= numbinario//10

num4= numbinario %10
dec4= num4**4
numbinario= numbinario//10

num5= numbinario %10
dec5= num5**5

print(dec1 + dec2 + dec3 + dec4 + dec5)






