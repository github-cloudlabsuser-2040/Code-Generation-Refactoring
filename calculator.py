#MiPrimeraCalculadora
# Autor: Nolfa LAbbe
# Fecha: 2024/11/20
# Descripcion: Calculadora que suma, resta, multiplica y divide dos numeros
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b
def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    return int(input("Seleccione una opcion: "))
while(True):
    opcion=menu()
    if(opcion==5):
        break
    a=float(input("Ingrese un numero: "))
    b=float(input("Ingrese otro numero: "))
    if(opcion==1):
        print("La suma es: ",suma(a,b))
    elif(opcion==2):
        print("La resta es: ",resta(a,b))
    elif(opcion==3):
        print("La multiplicacion es: ",multiplicacion(a,b))
    elif(opcion==4):
        print("La division es: ",division(a,b))
    else:
        print("Opcion invalida")    
print("Fin del programa")
1