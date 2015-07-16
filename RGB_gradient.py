color_1 = (0,146,0)

color_2 = (0,230,253)

def color_gradient(color_1,color_2,incs): #for R,G,B touples and at least 2 incs
    delta_R = color_1[0] - color_2[0]
    delta_G = color_1[1] - color_2[1]   
    delta_B = color_1[2] - color_2[2] 
    print  delta_R, delta_G, delta_B  
    
    return

color_gradient(color_1,color_2,1)

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

hex_to_rgb("#ffffff")             #==> (255, 255, 255)
hex_to_rgb("#ffffffffffff")       #==> (65535, 65535, 65535)
rgb_to_hex((255, 255, 255))       #==> '#ffffff'
rgb_to_hex((65535, 65535, 65535)) #==> '#ffffffffffff