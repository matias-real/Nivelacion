# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:45:11 2019

@author: USUARIO
"""
import numpy as np

a = np.arange(1,12,2)    #Crea un arreglo con el primer elemento igual a 1 y el ultimo igual a 12, con diferencia de 2 entre cada numero.

b = np.linspace(1,12,6)   #Crea un arreglo con "floats" partiendo del 1 y terminando con 12, con 6 elementos igualmente espaciados.

b.reshape(3,2)   #Cambia la forma del arreglo a 2 diemnsiones. Pero el arreglo original sigue igual (no guarda los cambios).
#Para guardar los cambios tendria que ser: b = b.reshape(3,2).

b.size   #Entrega la cantidad de elementos que tiene el arreglo sin importar la dimension.

b.shape     #Entrega la forma del arreglo

b.type    #Entrega el tipo de datos. en python por default es float 64.

b.itemsize    #Entrega cuanta memoria, en bytes, usa cada elemento.

b < 4   #Entrega true o false en la posicion del elemento dependiendo de si cumple con la condicion o no.

b*3    #Multiplica cada elemento por 3. Pero el arreglo original sigue como estaba antes (No modifica al arregglo original).

c = np.zeros((3,4))      #Nos da un arreglo lleno de ceros (floats64).

d = np.array([2,3,4], dtype=np.int16)    #Entrega un arreglo con el tipo de datos int16.

e = np.random.random((2,3))    #Entrega un arreglo con numeros aleatorios enttre 0 y 1 (2 filas y 3 columnas).

f = np.random.randint(0,10,5)   #Crea un arreglo con numeros int entre 0 y 10 (incluyendolo), con 5 elementos.

f.sum()   #Entrega la suma de los valores del arreglo.

f.max()    #Entrega el maximo valor del arreglo.

f.var()   #Entrega la varianza del arreglo.

f = f.reshape(3,2)   #Cambia la forma del arreglo a dos dimensiones.

f.sum(axis=1)   #Entrega la suma de los elementos del eje 1.

data = np.loadtxt("data.txt", dtype =np.uint8, delimiter= ",", skiprows=1)   #Sirve para iportar archivos de texto facilmente.

t = np.arange(10)    #Crea un arreglo del 0 al diez.

np.random.shuffle(t)   #Ordena el arreglo de manera aleatoria.





   








