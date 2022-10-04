#Condicional IF

#El condificonal if sirve para condicionar si cumple con la condicion ejecuta cierto codigo si no ejecuta algo mas:

#Ejemplo

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
