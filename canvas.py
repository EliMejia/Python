#CANVAS

""" 
Para imprimir en el lienzo se debe crear una funcion y 
un controlador del lienzo 
"""

#Ejemplo:

import simplegui

def draw(canvas):
                  #("texto",[tamanio],tamanio_letra,"color")
  canvas.draw_text("HELLO",[100,100],12,"white")
                     #([tamanio],radio,grosor,"color")
  canvas.draw_circle([100,100],2,2,"red")
  
frame=simplegui.create_frame("Text Drawing",300,200)
frame=set_draw_handler(draw)

frame.start()

