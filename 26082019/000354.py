# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 21:22:48 2019

@author: USUARIO
"""

d = {}   #Para crear un diccionario se usan parentesis de llave en vez de corchetes.
d["Matias"] = 23  #Para agregar elementos al diccionario se hace de esta manera.
d["Rodrigo"] = 30    #En diccionarios, los valores pueden ser de cualquier tipo pero las llaves no (tipos mas comunes para llaves son strings o numeros).     
d["Max"] = 22

for llave, valor in d.items():   #Este for sirve para recorrer el diccionario.        
    print "Llave:"
    print llave
    print "Valor:"
    print valor
    print ""