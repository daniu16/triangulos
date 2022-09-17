# determinar con los lados de un triangulo se este es un triangulo

print("----------------------------------------------------------")
print("--se determinara si con los lados dados es un triangulo---")
print("----------------------------------------------------------")

# input

a= int(input("ingrese el valos del primer lado: "))
b= int(input("ingrese el valos del seguno lado: "))
c= int(input("ingrese el valos del tercer lado: "))

#processing

if a+b>c:
    if a+c>b:
        if b+c>a:
            print("es un triangulo")
        else:
            print("no es un triangulo")  
    else:
        print("no es un triangulo")
else:
    print("no es un triangulo")