# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:36:47 2019

@author: USUARIO
"""
from skimage import io
import numpy as np
import matplotlib as plt

a = np.zeros(10)   #Crea un arreglo solo con valores "0", segun la cantidad que le demos dentro del parentesis.
                  #El tipo de datos del arreglo que crea es "float".

a.shape     #Entrega la forma del arrelo (filas y columnas).

a.shape = (10,1) #Cambia la forma del arreglo a 10 filas y 1 columna.
    
a = np.ones(10)   #Crea un arreglo solo con valores "1", segun la cantidad que le demos dentro del parentesis.
                  #El tipo de datos del arreglo que crea es "float".

b = np.empty(3)   #Crea un arreglo vacio de 3 "espacios".
 
c = np.linspace(2,10,5)   #Crea vector que que comienza en 2 y termina en 10, con 5 elementos (tambien floats).

d = np.array([10,20])   #Crea el arreglo [10,20]

lista = [1,2,3,4,5]
e = np.array([lista])    #Tambien se puede usar para crear arreglos con listas.

f = np.random.randint(10, size=6)    #Crea un arreglo de 6 elementos con numeros aleatorios entre 0 y 9.

g = f[0:2]     #Crea un arreglo con los primeros dos elementos del arreglo f.

photo = io.imread("foto.jpg")    #Sirve para leer fotos como arreglos numpy

plt.imshow(photo)     #Muestra la foto

plt.imshow(photo[::-1])  #Con esto la foto se gira en 180°.

plt.imshow(photo[:,::-1])    #Cn esto la foto queda como reflejada en un espejo.

plt.imshow(photo[50:150, 150:280])      #Toma parte de la foto, desde la fila 50 hasta la fila 150 y desde la columna 150 hasta 280.

np.sum(photo)   #Entrega la suma de todos los elementos en photo

np.max(photo)   #Entrega el maximo valor de photo

r = np.array([1,2,3,4,5])   #Arreglo de 5 elementos

r < 3   #Entrega un arreglo con True o False en la posicion del elemento, de acuerdo con si cumple la condicion o no.

r[r<3]   #Entrega un arreglo con los elementos que cumplpen la condicion

photo_masked = np.where(photo > 100,255,0)  #   Cuando  photo es mayor que 100 se reemplaza por 255 y cuando no, se reemplaza por 0. Con esto cambiamos los tonos de la imangen photo

a_array = np.array([1,2,3,4,5])
b_array = np.array([6,7,8,9,10])

a_array + b_array     #Suma cada uno de los valores con el correspondiente en el otro arreglo. Se puede hacer con multiplicacion, division y resta.

a_array @ b_array    #Se obtiene el producto punto entre los arreglos

plt.imshow(photo[:,:,0].T)   #Entrega la matriz traspuesta

w = np.array([5,2,1,3,4])

np.sort(w)   #Ordena el arreglo w
    





