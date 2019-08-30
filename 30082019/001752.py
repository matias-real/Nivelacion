# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 21:36:32 2019

@author: USUARIO
"""

from matplotlib import pyplot as plt
plt.style.use('grayscale')   #Sirve para cambiar el estilo del grafico

edades_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]  #Valores que van en el eje x

dev_y =  [38496, 42000, 46752, 49320, 53200,   #Valores que van en el eje y
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_y = [45372, 48876, 53850, 57287, 63016,    #Valores que van en el eje y para otra curva
            65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437,    #Valores que van en el eje y para otra curva
            56373, 62375, 66674, 68745, 68746, 74583]


plt.plot(edades_x, dev_y, color ="k", linestyle="--", marker="." ,label="Cualquier persona")    #Primero se pone el eje "x" y despues el "y". Con label le estoy poniendo nombre a la curva
#"K--" La K corresponde al color negro oara la linea y -- sirve para que la linea sea punteada 
#Marker = "." Le pone una marca de punto a la curva y marker="o" hace lo mismo pero le pone una marca mas grande

plt.plot(edades_x , py_dev_y, color="g", marker ="o", linewidth=3 ,label="Programadores")    #Con esto estoy graficando otros datos (para obtener mas de una curva en el grafico)
#"g" La g corresponde al color verde y como no le entregue formato para la linea python entiende que es la normal continua 

plt.plot(edades_x , js_dev_y, color="#adad3b", marker ="o", linewidth=3 ,label="JavaScript")


plt.title("salario medio (USD) por edad")   #Le pone titulo al grafico, para hacerlo mas explicativo
plt.xlabel("Edades")    #Le pone titulo al eje x
plt.ylabel("Salario medio (USD)")    #Le pone titulo al eje y
plt.legend()   #Esto sirve para que funcione el label de la linea 18 y 20

plt.grid(True)    #Le pone lineas verticales y horizontales al grafico para que quede cuadriculado

plt.savefig("plot.png")   #Guarda la imagen en el directorio actual
plt.show ()    #Con esto se imprime el grafico


