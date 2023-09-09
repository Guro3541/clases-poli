print ("Informacion acerca de gastos de combustible\n")

km = int(input ("ingrese la cantidad de kilometros: "))
precio = int(input("ingrese el precio del litro de combustible: "))
kml = int(input("cuantos km realiza con un litro de combustible: "))
print ("\n")
consumo = km / kml
gasto = consumo * precio 
print ("La cantidad de nafta utilizada es: " , round(consumo,2) , "litros")
print ("El gasto en cobustible es: " , round(gasto,2) , "pesos")