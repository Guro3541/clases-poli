'''
Actividad 23:
Un vehículo parte de la ciudad de Córdoba y se dirige a Rosario, por
autopista. La distancia aproximada entre ambas ciudades es de 400 km, el
vehículo se desplaza a una velocidad promedio de 122 km/h.
Desarrolle un programa que calcule el tiempo total en horas que demorara
ese vehículo en llegar a Rosario, no es necesario convertir a horas, minutos y
segundos, exprese el resultado como un número real
'''
ciu_part = input("\nIngrese ciudad de partida: ")
ciu_lleg = input("\nIngrese ciudad de llegada: ")
dist = int(input("\nIngrese la distancia aproximada: "))
vel = int(input("\nIngrese la velocidad a la que se desplaza: "))
tiem_demo = dist/vel
print ("\nEl tiempo de demora entre: "+(ciu_part), "y" , (ciu_lleg), "es de", round(tiem_demo), "horas aproximadamente")

