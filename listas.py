#LISTAS

"""
Son una coleccion de objetos, que permiten mantener
datos que se corresponden mutuamente,sin tener muchas
variables para guardarlos
"""

#CREATE

#Lista vacia
my_list=[]

#Lista de numeros
1=[0.1.2.3]

#Lista de cadenas 
2=["Hola","Eli"]

#Lista de listas
3=[[2,3],['a','b']]

#ACCESS

#Longitud de la cadena
print len(my_list), len(1)

print "Primer elemento",2[0]
print "Segundo elemento",3[1]

#Retrocede e imprime
print 1[-1]

#UPDATE

#En la lista 1, posicion 2 coloca un 4
1[2]=4 

print 1
