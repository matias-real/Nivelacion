# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 01:44:14 2019

@author: USUARIO
"""

def funcion3(x,y): #Una funcion puede tener mas de un parametro (se separan por comas).
    return x + y #La funcion3 tiene 2 parametros y devuelve, guarda o retorna la suma de estos parametros.
    
funcion3(25,3) #Esta linea retorna (pero no imprime) la suma de 25 + 3, osea 28.
#Pero para imprimirlo se debe asignar a una variable e imprimir esa variable. Se procede de la siguiente forma:

a = funcion3(25,3) #Esta linea guarda el valor de 28 en la variable a
print a #Esta linea imprime el resultado (28)

#Tambien se puede imprimir si asignarle el valor a una variable, de la siguiente manera:
print funcion3(25,3) #Esto tambien imprime el resultado pero queda mas ordenado el codigo asignando el valor a una variable.


