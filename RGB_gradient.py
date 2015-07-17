import math

print "Started"

incs = 100

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

color_1 = (101,146,0)

color_2 = (0,230,253)

def color_gradient(input_colors,incs): #for R,G,B touples and at least 2 incs
    color_1 = input_colors[0]
    color_2 = input_colors[1]
    delta_R = []
    delta_G = []  
    delta_B = []

    color_list= []
    
    num_colors = len(input_colors)   
    sub_gradients = num_colors - 1
      

    
    print "Number of input colors: ", num_colors
    if num_colors > incs:
        print "Error: number of colors cannot be greater than the number of increments"

    for indx in range(sub_gradients):
        print "color:", indx

  
        delta_R.append(input_colors[indx+1][0] - input_colors[indx][0])
        delta_G.append(input_colors[indx+1][1] - input_colors[indx][1]) 
        delta_B.append(input_colors[indx+1][2] - input_colors[indx][2])
        print  delta_R, delta_G, delta_B 
        inc_R = float(delta_R[indx])/float((incs-1))
        inc_G = float(delta_G[indx])/float((incs-1))
        inc_B = float(delta_B[indx])/float((incs-1))
        print "inc_R ",inc_R      
        for i in range(incs):
    #        print i 
            color_temp = rgb_to_hex((int(input_colors[indx][0] + inc_R*i ),int(input_colors[indx][1] + inc_G*i ),int(input_colors[indx][2] + inc_B*i )) )
            print color_temp
            color_list.append(color_temp)
    return color_list





import matplotlib.pyplot as plt


x = [x for x in range(4*incs)]
y = x


plt.axes()
plt.scatter(x, y,s=900, linestyle='-', c=color_gradient([(181,10,89),(0,230,253),(18,210,89),(50,120,200),(250,20,2)],incs), marker="o",edgecolors='none')
plt.axis('scaled')
plt.show()

print "Finished"