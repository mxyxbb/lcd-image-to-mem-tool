#!/usr/bin/env python

# vim: set ai et ts=4 sw=4:




from PIL import Image
from PIL import ImageSequence
import sys
import os



if len(sys.argv) < 2:
    print("Usage: {} <image-file>".format(sys.argv[0]))
    sys.exit(1)

fname = sys.argv[1]
clear_name=fname[0:fname.index('.')] #名字去除后缀.gif
# print(fname[0])
print(fname[0:fname.index('.')])
# L.index(2)

img = Image.open(fname)
img_list=[]
i = 0
for frame in ImageSequence.Iterator(img):
    frame = frame.convert('RGB')
    resized_image = frame.resize((128, int(frame.size[1] * 128 / frame.size[0])))
    resized_image.save("resized_image%d.png" % i)
    img_list.append(resized_image) 
    i += 1
img_numbers=i
print(img_list)
img_size = str(img_list[0].width)+"x"+str(img_list[0].height)
# if img.width == 128 or img.height == 128:
#     print("Loading: 128x128 image")
#     img_size="128x128"
# elif img.width == 128 or img.height == 160:
#     print("Loading: 128x160 image")
#     img_size="128x160"
# else:
#     print("error: can find 128x160/128x128 image")
#     sys.exit(2)


with open("picdata_gif_"+clear_name+".h","w") as f: 
    # print('Hello, world!', file=f)
    # 打印gif内的所有图片数据
    for i in range(0,img_numbers):
        img=img_list[i]
        print("// "+clear_name+"_"+img_size+" image data", file=f)
        print("const uint16_t "+clear_name+"_"+img_size+"_%d[] = {" % i, file=f)
        for y in range(0, img.height):
            s = ""
            for x in range(0, img.width):
                (r, g, b) = img.getpixel( (x, y) )
                color565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | ((b & 0xF8) >> 3)
                s += "0x{:04X},".format(color565)
            print(s, file=f)

        print("};", file=f)
        print(clear_name+"_pic%d,ok" % i)
    print("", file=f)
    # 打印图片列表
    print("// "+clear_name+"_"+img_size+" image data list", file=f)
    print("const uint32_t "+clear_name+"_"+img_size+"_list[] = {", file=f)  
    for i in range(0,img_numbers):
        print(clear_name+"_"+img_size+"_%d," % i, file=f)
    print("};", file=f)
    

        
