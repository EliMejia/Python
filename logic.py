
#Logic

"""
True(T) 
False(F)

a   Not a
T     F 
F     T

a   b      a and b    a or b 
F   F        F          F
F   V        F          T 
T   F        F          T
T   T        T          T

"""

#Ejemplo 1

a=True 
b=False

print not a 
print a and b 
print a or b

#Ejemplo 2

a=True 
b=False 
c=True 
d=False

print(a and b) or (c and (not d))
