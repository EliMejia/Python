#EVENTOS

"""
La programacion por eventos consiste en esperar una accion

Los eventos pueden ser de diferentes acciones:
1.- INPUT
  -Button
  -Text_box
2.- MOUSE
  -Click
  -Drag
3.-KEYBOARD
  -key_dow
  -key_up
4.-TIMER
"""

# Ejemplo:Cada determinado tiempo se debe imprimir tick!

#se debe importar la libreria 
import simplegui 

#se crea una funcion 
def tick(): 
  print "tick!"

#se crea un temporizador
timer= simplegui.create_timer(1000,tick) 

#Inicializar el temporizador
time.start()


