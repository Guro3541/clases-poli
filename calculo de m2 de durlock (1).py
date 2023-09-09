
print ("=================================")
print ("Calculadora de metros de durlock")
print ("=================================\n")

met_par1 = float(input("Ingrese los metros de la primera pared: "))
met_par2 = float(input("Ingrese los metros de la segunda pared: "))

cant_paredes1 = int(input("Ingrese cantidad de paredes 1: "))
cant_paredes2 = int(input("Ingrese cantidad de paredes 2: "))

altura = float(input("Ingrese la altura de la pared: "))

ancho_vent = float(input("Ingrese el ancho de la ventana: "))
alto_vent = float(input("Ingrese el alto de la ventana: "))
ventana = ancho_vent * alto_vent
ancho_puerta = float(input("Ingrese el ancho de la puerta: "))
alto_puerta = float(input("Ingrese el alto de la puerta: "))
puerta = ancho_puerta * alto_puerta

cant_placas_pared = (met_par1*2 + met_par2*2 - ventana - puerta) * altura/2.88
print ("==================================================\n")
print (("Usted necesita" ) , round(cant_placas_pared, 2) , ("placas"))
print ("==================================================\n")

print("Calculadora de metros de durlock cielorraso\n")
lar_techo = float(input("Ingrese el largo del techo: "))
ancho_techo = float(input("Ingrese el ancho del techo : "))
cant_placas_cielorraso = lar_techo*ancho_techo/2.88
print ("==================================================\n")
print (("Usted necesita" ) , round(cant_placas_cielorraso, 2) , ("placas\n"))


