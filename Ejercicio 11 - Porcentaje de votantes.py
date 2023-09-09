#  Ejercicio 11 - Porcentaje de votantes
print ("Ejercicio 11 - Porcentaje de votos obtenidos\n")

cant_electores = int(input("Ingrese la cantidad de votantes habilitados: "))
cand_a = int(input("\nIngrese cantidad de votos obtenidos candidato a: "))
cand_b = int(input("\nIngrese cantidad de votos obtenidos candidato b: "))

if cand_a > cant_electores:
    print ("la cantidad ingresada no corresponde")

porcentaje_a = (cand_a  * 100) / cant_electores
porcentaje_b = (cand_b  * 100) / cant_electores

print ("\nEl porcentaje obtenido por el candidato a es: ", round(porcentaje_a , 2) ,"%")
print ("\nEl porcentaje obtenido por el candidato b es: ", round(porcentaje_b , 2) , "%")
