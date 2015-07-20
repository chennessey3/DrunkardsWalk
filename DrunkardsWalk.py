import random
import math
import matplotlib.pyplot as plt
import time
import RGB_gradient as RGB


x = [0]
y = [0]

for i in range(10000):
#    time.sleep(.11)
    theata = math.radians(360*random.random())
    length = 10 * random.random()
    x_inc = (length*math.cos(theata))
    y_inc = (length*math.sin(theata))
    x.append(x_inc + x[i])
    y.append(y_inc + y[i])

#print x,y
plt.axes()

#pick a random number of colors
max_number_colors = 3
number_of_colors = int(math.ceil(random.random()*(max_number_colors)))
print "number of colors:", number_of_colors
input_colors = []
for color in range(number_of_colors):
    input_colors.append(RGB.random_color())
print "input colors:",input_colors


plt.scatter(x, y, linestyle='-', c=RGB.color_gradient(input_colors,(len(x)/(number_of_colors))), marker="o",edgecolors='none')

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