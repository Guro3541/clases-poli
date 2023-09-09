# Ejercicio 28
#  Asignacion de variables
print ("Sistema para calcular horas extras de un empleado")
print ("*"*50)

h_trab = 0
pag_diur = 5234
pag_noc = 8057.57

#  Entrada de datos
turno = int(input ("Ingrese turno en el que trabajo el operario: "))
if turno > 2 :
    
    print ("Turno no valido")
else :
    h_trab = int(input ("Ingrese las horas que trabajo el operario: "))

# Proceso
    if turno == 1 :
        print ("El operario cobrara: ",(pag_diur*h_trab))
    elif turno == 2:
        print ("\nEl operario cobrara: ",(pag_noc * h_trab))
    
print ("*"*50)
print ("\nFin.")