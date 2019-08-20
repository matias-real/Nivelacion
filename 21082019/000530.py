# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 11:32:30 2019

@author: USUARIO
"""

a = [3, 10, -1] #Listas van entre corchetes.

a.append(4) #La funcion append agrega un elemento al final de la lista.

#Una lista puede tener distintos tipos de datos en ella.
a.append("hola") #Esto agrega el string hola al final de la lista.

#Hasta ahora la lista a = [3, 10, -1, 4, "hola"]

a.append([1,2]) #Crea una lista con los valores 1 y 2 y agrega esta lista en la ultima posicion de la lista "a".

a.pop() #Elimina el ultimo elemento de la lista, en este caso la lista [1,2].

#No olvidar que en las listas el primer elemento tiene indice 0.

b = a[0] #Con esto le estoy asignando a "b" el primer elemento de la lista "a".
#b = 3

a[0] = 7 #Con esto estoy cambiando el valor del primer elemento de la lista "a" y reemplazandolo por un 7.


