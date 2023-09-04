#Escribe un programa que pida al usuario dos números y muestre el número mayor o si son iguales.
print("Ingresa 2 numeros por favor")
print("Te demostrare cual es el mayor")
numero1=int(input("Ingresa un numero: "))
numero2=int(input("Ingresa otro numero: "))

if numero1>numero2:
    print ("El mayor es"+"_"+str(numero1))
if numero2>numero1:
    print ("El mayor es"+"_"+str(numero2))
if numero2==numero1:
    print("Los numeros son iguales")