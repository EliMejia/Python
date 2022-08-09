# Python

CodeSkulptor: Es un ambiente desarrollado de Python, no necesita descarga.

Corre las lineas de codigo y el resultado lo muestra en pantalla.
Es para guarda, al presionarlo el URL cambia, se le asigna un nombre aletario que es utilizado en la nube
Se desacarga el programa en la computadora
Si fue descargado puede ser abierto desde este boton
Al presionarlo se guarda pero la version final sin poder ver las versiones anteriores
Borra lo de la consola para volver a ejecutar

Expresiones Aritmeticas

Numeros enteros con signo Ejemplo:1, -3 ints o integers
Numeros fraccionarios con signo Ejemplo: 2.4, -5.28 floats o numeros de punto flotante 
Si no se sabe con que numero se esta trabajando esta type(numero), devuelve si es int o float Ejemplo type(3), type(2.65)

Operadores Aritmeticos 
+   plus Addition
-   minus Subtraction
*   times Multiplication
/   divide by Division
**  power Exponentiation


Jerarquia 
Parentesis y lo que tenga mas peso: Exponentes,multiplicacion, division, adicion y sustraccion

Variables 

Para facilitar la programacion existen varibles que sirven para almacenar informacion que se puede utilizar en mas de una ocasiones, el valor de la varible 
puede ir cambiando conforme el desarrollo:

my_name="Eli"
print my_name

Puede contener guiones bajos o numeros pero no pueden ir al inicio Ejemplo:

Error:
1321_name

Correcto:
name_1321

Funciones 

Una funcion es un pedazo de codigo que se define para ser ejecutando, entonces solo se ejecuta el codigo de una funcion cuando se invoca esa funcion.

Estructura: Con Parametros 
     
           def nombre_funcion(param1,param2..):
           cuerpo de la funcion 
           return variable (para retornar valores puede o no ir)

Ejemplo: 
      
          def triangle_area(base,height):
          area=(1.0/2)*base*height
          return area

       
Sin Parametros 
    
         def nombre_funcion():
         cuerpo de la funcion
         return varible (para retornar valores puede o no ir)

Ejemplo:

         def hello():
         print "Hello, word!"
         

Viz Mode 

Permite correr el programa paso por paso, para depurar en caso de que haya errores, es un modo mas tedioso pero si hay error puede ser un auxiliar para encontrarlo.
1.- En la parte superior derecha esta el modo Viz, borrar todo lo de la ventana y pegar el codigo a analizar.
         
Operadores

% obtener el residuo de una division 

Ejemplo: num=49
         tema=num//10
         ones=num%10
         print tema, ones
         
         Salida 4, 9
        
Operadores de Comparacion 
< Menor que
>>Mayor que 
<= Menor o igual que
>= Maor o igual que 
== igual que 
=! diferente que

Ejemplo 

a= 7 > 3
print a
 x=5
 y=5
 b=x>y
 print b
 
 c='Hello'=='hello'
 print c
 
 d=20.6<=18.3
 print d
 
 Condicional IF 
 
 El condificonal if sirve para condicionar si cumple con la condicion ejecuta cierto codigo si no ejecuta algo mas:
 
 Ejemplo 
 
    def greet(friend,money):
       if friend and (money>20):
       print "Hi!"
       money=money-20
       elif friend:
        print "Hello"
         else:
         print "Ha ha"
         money=money+10
         money
         
         money=15
         money=greet(true,money)
         print "money:",money
         
Proyecto 2
https://py2.codeskulptor.org/#user49_tA6xqSiww8_1.py
Proyecto 3
https://py2.codeskulptor.org/#user49_Wo4iB2m6Y5_0.py
Proyecto 4
https://py2.codeskulptor.org/#user49_TRL5NF1oNkkXw3P.py

https://py2.codeskulptor.org/#user49_oQewxe77Ga_0.py

 



Convertir 

Para convertir int o float en cadena:
       
       hour=3
       ones=hour%10
       tens=hour// 10
       print str(tens),str(ones),":00"
       
Importar

Se pueden importar librerias para utilizar operadores matematicos de forma mas facial

import simplegui
import math
import random Numeros Aleatorios

Ejemplo: math.pi

Logic 

True(T)
False(F)

a  Not a
T  F
F  T

a  b   a and b    a or b
F  F      F          F
F  V      F          T
T  F      F          T
T  T      T          T

Ejemplo 1 

a=True
b=False

print not a
print a and b
print a or b


Ejemplo 2

a=True
b=False
c=True
d=False

print(a and b) or (c and (not d))



       


