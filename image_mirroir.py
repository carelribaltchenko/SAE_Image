from PIL import Image

i=Image.open("hall-mod_0.bmp")
sortie = i.copy()
for y in range(i.size[1]):
    for x in range(i.size[0]):
        c=i.getpixel((x,y))
        sortie.putpixel((i.size[0]-1-x,y), c)
sortie.save("Imageout1.bmp")

