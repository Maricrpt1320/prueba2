#importar libreria (recetas/ codigos prefabricados)
import math



#declaro el bucle/ciclo/repeticion/lavuelta
print('Empanadas Alejandra')
print('********')
print('0. Digita 0 para salir')
print('1. Digita 1 para calcular la raíz cuadrada de un #')
print('2 Digita 2 para calcular la potencia 2 de un #')
print('********')
#Variable controladora
opcion=1
while(opcion!=0):
#Variable controladora
 opcion=int(input('Digita una opción: '))
#pregunte por la opción
 if(opcion==0):
  break
 elif(opcion==1):
  numero=int(input("Digita un número: "))
  raiz=math.sqrt(numero)
  print(f'la raiz de {numero} es {raiz}')
 elif(opcion==2):
  numero=int(input("Digita un número: "))
  potencia=math.pow(numero,2)
  print(f'La potencia de numero es: {potencia}')
 else:
   print('No existe esa opción') 
   