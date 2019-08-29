# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:04:01 2019

@author: USUARIO
"""
#VIDEO DE 3 HORAS!!!!
import numpy as np

a = np.array([2,3,4], dtype = np.int16)    #Crea un arreglo con el tipo de datos int16
a[0] = 10.6    #Si un arreglo es de tipo int y le  agrego un float, python lo va a truncar para poder agregarlo  al arreglo.


c = np.array([[10,11,12],[20,21,22]])    #Crea unn arreglo de dos dimensiones
c.ndim   #Entrega la cantidad de dimensiones que tiene el arreglo

c.size  #Entrega el numero total de elementos del arreglo.

c.nbytes  #Entrega  la cantidad de memoria que usa el arreglo.

c[0,0]   #Entrega el primer elemento del arreglo (10) (en listas seria c[0][0]).

c[0]   #Entrega la primera dimension del arreglo (10,11,12)

d = np.array([10,11,12,13,14])
d[1:3]    #Entrega un arreglo con los elementos desde la posicion 1 hasta la 3 (sin incluir la 3) ([11,12])

d[1:-2]  #Entrega un arreglo con los elementos desde la posicion 1 hasta la penultima (sin incluir el penultimo elemento) ([11,12])

#Si se omite el primer indice o el segundo, se asume que es el primero o el ultimo, respectivamente 

d[::2]   #Esto entrega un arreglo desde el princio hasta el final, agregando elementos cada 2 elementos ([10,12,14]).

c[2:, 2:]   #Entrega  un arreglo desde la fila 2 hasta el final y desde columna 2 hasta el final


e = np.arange(25).reshape(5,3)
e[4]   #Entrega [20,21,22,23,24]   (Ejercicio minuto 42)

d.copy  #Crea una copia del arreglo d para poder trabajar con el sin modificar el arreglo original

f = np.array([3, -1, -2, 4, -6, 8])

negativos = f < 0   #Esto sirve solo para hacer el codigo mas entendible (no es necesario ponerle nombre)
f[negativos]   #Entrega un arreglo con todos los elementos negativos del arreglo f.

(f < 10).any()   #Toma el valor True porque todos los elementos del arreglo son menores que 10

g = np.array([4, -8, 3, -2, -1, 9])

f > g  #Compara por posicion de cada arreglo y si es correcta la afirmacio entre True y si es falsa entrega False. Entregaria ([False, True, False, True, False, False]) 

e[e % 3 == 0]    #Entrega un arreglo con los numero divisibles por 3 (ejercicio 013058).

np.sum(g)   #Suma todos los valores del arreglo.




 
 
 



