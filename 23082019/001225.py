# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:34:54 2019

@author: USUARIO
"""

lista = [7, 5, 4, 3, 1, -2, -3, -5, -7]  #Lista que va descendiendo de izquierda a derecha.
#Queremos obtener la suma de los numeros negativos solamente.

i = -1   #Fijo el indice para sumar en el while.
suma = 0  #Variable que almacena la suma de los numeros negativos.

while True:   #Con esto hago que siempre corra el while, a menos que llegue a la sentencia break.
    
    suma += lista[i]   #Como i lo fije en -1, en la primera iteracion lista[-1] me entrega el ultimo valor de la lista.
    i -= 1    #Le resto 1 para ir recorriendo la lista de derecha a izquierda. 
    
    if lista[i] >= 0:   #Con esto compruebo que los numeros que estoy sumando a suma sean negativos. 
        break     #Si se cumple la condicion del if, la sentencia break le dice al while que se detenga.
        
print suma   #Como esto esta afuera del while me va a entregar la suma final de los numeros negativos.