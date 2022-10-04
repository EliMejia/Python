# Qué tecla se presiona?

"""
Es posible saber que tecla esta siendo presionada 
y en base a ello realizar alguna actividad
"""

#Ejemplo dibujar la tecla que se presiona

import SimpleGUI
current_key=''

def keydown(key):
  global current_key
  current_key=chr(key)

def keyup(key):
  global current_key
  current_key=''
  
def draw(canvas):
  canvas.draw_text(current_key,[10,25],20,"Red")
  
frame=simplegui.create_frame("Echo",35,37)

#Tecla Presionado
frame.set_keydown_handler(keydown)

#Tecla No Presionada
frame.set_keyup_handler(keyup)

frame.set_draw_handler(draw)

frame.start
