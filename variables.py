#VARIABLES

""" Para facilitar la programacion existen varibles que sirven para almacenar informacion que se puede
utilizar en mas de una ocasiones, el valor de la varible puede ir cambiando conforme el desarrollo: """

#EJEMPLO

my_name="Eli" 

print my_name


#Puede contener guiones bajos o numeros pero no pueden ir al inicio Ejemplo:

#Error: 1321_name

#Correcto: name_1321

"""
En programacion existen dos tipos de variables:

1.- GLOBALES: su valor se puede utilizar en todo el progtrama ademas de qie es posible cambiar su
valor en el transcurso de este.

2.- LOCALES: su valor solo se puede utilizar o modificar dentro de la funcion, las valiables 
locales son las que se definen dentro de una funcion

NOTA:Aunque el valor de la variable global cambie se puede utilizar en una funcion su valor
original con..... global nombre_variable
"""

#Ejemplo

num=4

def fun1():
  global num
  num=5
 
print num #El resultado sera 4 ya que todavia no se aplican los cambios
fun1() #Se llama a la funcion que cambia el valor del numero
print num #El resultado sera 5 ya que el cambio de valor fue hecho anteriormente en el numero
