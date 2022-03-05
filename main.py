#Ejemplo de estaciones

mes=input('Digita un mes del año:')
print(f'El mes digitado fue {mes}')


if(mes == "Diciembre" or mes == "Enero" or mes == "Febrero"):
 print ('Estás en invierno')
elif(mes == "Junio" or mes == "Julio" or mes == "Agosto"):
 print ('Estás en verano')
elif(mes == "Marzo" or mes == "Abril" or mes == "Mayo"):
 print ('Estás en primavera')   
elif(mes == "Septiembre" or mes == "Octubre" or mes == "Nombre"):
 print ('Estás en otoño')
else:
 print ('No existe tu dato')     
 
 
 