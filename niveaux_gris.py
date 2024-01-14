from PIL import Image
i=Image.open("IUT-Orleans.bmp")
sortie = i.copy()
for y in range(i.size[1]):
    for x in range(i.size[0]):
        c=i.getpixel((x,y))
        print(x,y)
        sortie.putpixel((x,y), ((c[0]+c[1]+c[2])//3,(c[0]+c[1]+c[2])//3,(c[0]+c[1]+c[2])//3))
sortie.save("Imageout2.bmp")