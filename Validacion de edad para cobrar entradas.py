'''
Escribir un programa para una empresa
que tiene salas de juegos para todas las edades y
quiere calcular de forma automática el
precio que debe cobrar a sus clientes por entrar.
El programa debe preguntar al usuario la
edad del cliente y mostrar el precio de la entrada.
Si el cliente es menor de 4 años puede entrar gratis,
si tiene entre 4 y 18 años debe pagar 5€ y
si es mayor de 18 años, 10€.
'''
print ("----------------------------------------")
print ("Sistema para calcular quien paga entrada")
print ("--------------------------------------\n")
may_4men_18 = 5
may_18 = 10

edad = int(input("Ingrese su edad: "))
if edad < 4:
    print ("No debe pagar entrada")


if edad > 4 and edad <= 18:
    print ("Debe abonar: " , may_4men_18,("$"))


if edad > 18 :
    print ("Debe abonar: " , may_18,("$"))
print ("Fin.")

    
    
    
    
    
'''    
if renta > 20000 and renta <= 35000:
    abona = (renta * 20/100)
    print ("La renta anual a abonar es de: " , abona)
if renta > 35000 and renta <= 60000:
    abona = (renta * 30/100)
    print ("La renta anual a abonar es de: " , abona)
if renta >= 60000 :
    abona = (renta * 45/100)
    print ("La renta anual a abonar es de: " , abona)
    '''