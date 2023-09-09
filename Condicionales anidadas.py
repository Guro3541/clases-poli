print ("=============================================")
print ("Aprendiendo a usar las Condicionales anidadas")
print ("=============================================")

print ("Menu de opciones")
print ("===============")
print ("Presiona 1 para convertir de numero a palabra")
print ("Presiona 2 para convertir de palabra a numero")

opcion = int(input ("Ingrese la opcion deseada: "))

if opcion == 1:
    print ("Has elegido convertir de numero a palabra")
    numero = int(input ("Ingrese el primer numero a convertir: "))

if numero == 1:
   print ("El numero es uno")
elif numero == 2:
    print ("El numero es dos")    
elif numero == 3:
    print ("El numero es tres")
elif numero == 4:
    print ("El numero es cuatro")
elif numero == 5:
    print("El numero es cinco")
else :
    print ("El numero se desconoce")

print ("fin")

if opcion == 2:
    print ("Has elegido convertir de palabra a numero")

numero = str(input ("Ingrese la palabra convertir en numero: "))

if numero == 'uno':
    print ("El numero elegido es 1")
elif numero == 'dos':
    print ("El numero elegido es 2")
elif numero == 'tres':
    print ("El numero elegido es 3")
elif numero == 'cuatro':
    print ("El numero elegido es 4")
elif numero == 'cinco':
    print ("El numero elegido es 5")
else :
    print ("El numero se desconoce")
print ("Fin")