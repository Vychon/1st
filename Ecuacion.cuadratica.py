    #ecuacion cuadratica con una función
import math
def resultado(a,b,c):
    calculo1 = ((-b - math.sqrt(b*b - 4*a*c))/2*a)
    calculo2 = ((-b + math.sqrt(b*b - 4*a*c))/2*a)
    print(calculo1, calculo2)
resultado(1,1,-2)    
