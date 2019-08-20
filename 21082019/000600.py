# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 12:10:56 2019

@author: USUARIO
"""

#000600
c = ["platano", "manzana", "microsoft" ]
r = [1,2,3]

def cambio_primeroYultimo (a):     #Funcion para cambiar el primer y ultimo elemento de una lista de 3 elementos.
    b = []    #Creo lista vacia
    b.append(a[2])   #Agrego al final de mi lista vacia el ultimo elemento de mi lista de 3 elementos
    b.append(a[1])   #Mantengo el elemento de al medio en su posicion.
    b.append(a[0])   #Agrego al final de mi nueva lista el primer elemento de la lista de 3 elementos
    return b

cambio = cambio_primeroYultimo(r)
print cambio

#F