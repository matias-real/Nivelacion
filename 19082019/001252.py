# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:07:35 2019

@author: USUARIO
"""

e = 18 # Con un signo igual estoy diciendo que la variable de la izquierda tiene el valor de la derecha
f = 5 # Con un signo igual estoy diciendo que la variable de la izquierda tiene el valor de la derecha

if e < f: # Comando if sirve para decirle al codigo que revise si pasa algo, en este caso si es que e es menor que f
    print "e es menor que f" #Como el print esta identado dentro del if, imprimira esto solo si es que e es menor que f

elif e == f: # Luego de usar un if, si se quiere poner mas condicionantes se usa elif 
    print "e es igual a f" #Como el print esta identado dentro del elif, imprimira esto solo si es que e es igual que f
# El == se utiliza para corroborar que dos variables son iguales, por eso no se utiliza = en este caso sino ==.

else: #el comando else se utiliza para condicionar los casos restantes que quedan, en este caso seria que f sea mayor a e
    print "e es mayor a f" #Como el print esta identado dentro del else, imprimira esto solo si es que e es mayor que f
    
    