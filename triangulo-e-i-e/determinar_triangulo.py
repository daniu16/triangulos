# determinar que tipo de triangulo es

print("----------------------------------------------------")
print("--determinar si es isoseles equilatro y escaleno.---")
print("----------------------------------------------------")

# input

a= int(input("ingrese el valor del primer angulo:"))
b= int(input("ingrese el valor del segundo angulo:"))
c= int(input("ingrese el valor del tercer angulo:"))

#processing

if a+b+c==180:
    if a==b==c:
        print(" es un equilatero")
    elif a!=b:
        if a!=c:
            print(" es un isoceles")
    if a!=b!=c:
        print(" es un escaleno")
else:
    print("no es uhn tringulo")