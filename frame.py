import simplegui

#CREATE FRAME

#frame=simplegui.create_frame("Nombre_Frame,ancho,largo")
#Ejemplo

frame=simplegui.create_frame("Ejemplo",200,200)

#INICIALIZAR FRAME

frame.start()

#CREATE BUTTONS

#frame.add_button("texto_button,funcion_ejecuta,tamanio")
#Ejemplo

frame.add_button("imprimir",print,100)

#CREATE INPUT TEXT

#frame.add_input("Nombre_Input",Funcion_Ejecuta,Tamanio)
#Ejemplo

frame.add_input("Nombre",name,100)

