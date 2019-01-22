num1=int(input("Introduce el primer numero "))
num2=int(input("Introduce el segundo numero "))

var = int(input("¿Que desea hacer?\n1-Suma\n2-Multiplicacion\n3-Division\n4-Exponencial\n"))
resultado = False
if(var==1):
    resultado = num1 + num2
elif(var==2):
    resultado = num1*num2
elif(var==3):
    if(num2!=0):
       resultado = num1/num2
    else:
        print("resultado no valido")
elif(var==4):
    resultado = num1**num2
else:
    print("no exite esta opción")

print(resultado)
    
