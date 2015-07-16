import random
import math
import matplotlib.pyplot as plt


x = [0]
y = [0]

for i in range(500):
    theata = math.radians(360*random.random())
    length = 1 #0 * random.random()
    x_inc = (length*math.cos(theata))
    y_inc = (length*math.sin(theata))
    x.append(x_inc + x[i])
    y.append(y_inc + y[i])    
#print x,y
plt.axes()


plt.scatter(x, y, linestyle='-', c=str(random.random()), marker="o",edgecolors='none')

#def square(list):
 #   return [i ** 2 for i in list]
    
#x_sq =  square(x)   
#y_sq =  square(y)     
    
#sum= []    
    
#for indx, val in enumerate(x_sq):
 #   sum.append(val +y_sq[indx] )

#print "sum: ", sum

plt.axis('scaled')
plt.show()