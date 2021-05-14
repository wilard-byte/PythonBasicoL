
#Ejercicio 1
n = int(input("Introduce la altura del triangulo (entero positivo):"))

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")


    continue

#Ejercicio 2 
n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")


    continue


#Ejercicio 3
n = int(input("Introduce un numero entero positivo mayor que 2:"))

i = 2
while n % i !=0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n)+ " no es primo")


