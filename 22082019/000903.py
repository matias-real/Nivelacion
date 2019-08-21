# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:04:28 2019

@author: USUARIO
"""
#000903
suma = 0  #Variable que acumula la suma de los numeros menores que 100 y multiplos de 3 o 5. 
for i in range(100):    #Creo una lista con valores desde 0 hasta 99.
    if i % 3 == 0:      #Verifico si el numero de la lista es multiplo de 3.
        suma += i       #Si es asi, lo sumo a "suma".
        
    elif i % 5 == 0:    #Si el numero no es multiplo de 3 reviso si es multiplo de 5.
        suma += i       #Si es as, lo sumo a suma.
    
print suma   #Suma de todos los numeros multiplos de 3 o 5 y menores que 100.