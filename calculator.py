def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    
    
def exponencial(a,b):
    return a**b

opciones = {1:'Suma', 2:'Resta', 3:'Multiplicacion', 4:'Division', 5:'Exponencial', 6:'Salida'}

salir = 1

while salir:
    
    var = int(input("¿Que desea hacer?\n1-Suma\n2-Resta\n3-Multiplicacion\n4-Division\n5-Exponencial\n6-Salida\n"))

    if (var !=6):
        try:
            num1=int(input("Introduce el primer numero "))
            num2=int(input("Introduce el segundo numero "))
        except ValueError:
            print("Hay que introducir numeros")
            break
            
    resultado = False
    
    if(opciones[var]=='Suma'):
        resultado = suma(num1,num2)
        
    elif(opciones[var]=='Resta'):
        resultado = resta(num1,num2)
        
    elif(opciones[var]=='Multiplicacion'):
        if(num2!=0):
           resultado = multiplicacion(num1,num2)
        else:
            print("resultado no valido")
    elif(opciones[var]=='Division'):
        resultado = division(num1,num2)

    elif(opciones[var]=='Exponencial'):
        resultado = exponencial(num1,num2)
        
    elif(opciones[var]=='Salida'):
        salir = 0
    else:
        print("no exite esta opción")

    if (salir ==1):
        print("RESUTADO:" , resultado)
        print("\n\n")
