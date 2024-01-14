from PIL import Image

i=Image.open("IUT-Orleans.bmp")
sortie = i.copy()
for y in range(i.size[1]):
    for x in range(i.size[0]):
        c=i.getpixel((x,y))
        if (c[0]**2+c[1]**2+c[2]**2)>255*255*3/2:
            sortie.putpixel((x,y), (255,255,255))
        else :
            sortie.putpixel((x,y), (0,0,0))
sortie.save("Imageout3.bmp")