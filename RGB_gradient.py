import math

print "Started"

incs = 40

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

color_1 = (101,146,0)

color_2 = (0,230,253)

def color_gradient(color_1,color_2,incs): #for R,G,B touples and at least 2 incs
    color_list= []
    delta_R = color_2[0] - color_1[0]
    delta_G = color_2[1] - color_1[1]   
    delta_B = color_2[2] - color_1[2] 
    print  delta_R, delta_G, delta_B 
    inc_R = float(delta_R)/float((incs-1))
    inc_G = float(delta_G)/float((incs-1))
    inc_B = float(delta_B)/float((incs-1))
    print "inc_R ",inc_R      
    for i in range(incs):
#        print i 
        color_temp = rgb_to_hex((int(color_1[0] + inc_R*i ),int(color_1[1] + inc_G*i ),int(color_1[2] + inc_B*i )) )
        print color_temp
        color_list.append(color_temp)
    return color_list





import matplotlib.pyplot as plt


x = [x for x in range(incs)]
y = x


plt.axes()
plt.scatter(x, y,s=90, linestyle='-', c=color_gradient(color_1,color_2,incs), marker="o",edgecolors='none')
plt.axis('scaled')
plt.show()

print "Finished"