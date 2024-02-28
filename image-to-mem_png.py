#!/usr/bin/env python

# vim: set ai et ts=4 sw=4:

from PIL import Image
import sys
import os

if len(sys.argv) < 2:
    print("Usage: {} <image-file>".format(sys.argv[0]))
    sys.exit(1)

fname = sys.argv[1]
clear_name=fname[0:fname.index('.')] #名字去除后缀.png/jpg
print(fname[0:fname.index('.')])

img = Image.open(fname)
img = img.convert('RGB')
print("original pic size: "+ str(img.size))
resized_image = img.resize((128, int(img.size[1] * 128 / img.size[0])))
# if img.size[1]<img.size[0]:
#     resized_image = img.resize((128, int(img.size[1] * 128 / img.size[0])))
# else:
#     resized_image = img.resize((int(img.size[0] * 160 / img.size[1]), 160))
resized_image.save("resized_image_"+clear_name+".png")
img = resized_image
img_size = str(img.width)+"x"+str(img.height)
print("resized pic size: "+ str(img.size))
if img.width == 128:
    print("Loading: 128x"+str(img.height)+" image")
else:
    print("Can not convert a "+img_size+" size pic. Suppose a 128 width.")
    sys.exit(2)

with open("picdata_pic_"+clear_name+".h","w") as f: 
    print("// "+clear_name+"_"+img_size+" image data", file=f)
    print("const uint16_t "+clear_name+"_"+img_size+"[] = {", file=f)
    for y in range(0, img.height):
        s = ""
        for x in range(0, img.width):
            (r, g, b) = img.getpixel( (x, y) )
            color565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | ((b & 0xF8) >> 3)
            s += "0x{:04X},".format(color565)
        print(s, file=f)

    print("};", file=f)
    print(clear_name+"_pic,ok")
    print("", file=f)
