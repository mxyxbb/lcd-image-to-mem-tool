# LIB REQUIREMENT:
- Python Imaging Library(PIL)

use use the following command to install the library

```
sudo pip3 install pillow
```

# info
- python3.9 is used, but for other version it should be fine.
- arrays in .h file is encoded in RGB565 format.
- the array size can be seen by its name.
- .h file form a png/jpg file 
- .h file form a gif file includes a address list

.h file form a gif file looks like

![image](https://github.com/mxyxbb/lcd-image-to-mem-tool/assets/53026754/dce14fb7-7650-447b-91c1-0dcc9c666aa7)

the address list looks like

![image](https://github.com/mxyxbb/lcd-image-to-mem-tool/assets/53026754/0046d5aa-0af9-455a-99b6-2f00a2902773)

# how to use the tool:

- use the following command to generate from a .gif file

```
python image-to-mem_gif.py boygirl_dance.gif
```

then a picture sequence and a "picdata_gif_boygirl_dance.h" file will be created in your folder.

![image](https://github.com/mxyxbb/lcd-image-to-mem-tool/assets/53026754/7f808a5d-66a8-4ffd-b774-e852eb666176)

![image](https://github.com/mxyxbb/lcd-image-to-mem-tool/assets/53026754/99ca36db-ca6f-444d-b526-1720b3aa7a9b)


- use the following command to generate from a .png/jpg file
```
python image-to-mem_png.py ghulmil_com.jpg
```

then a picture.png and a "picdata_pic_ghulmil_com.h" file will be created in your folder.

![image](https://github.com/mxyxbb/lcd-image-to-mem-tool/assets/53026754/705b050a-ee52-4316-99ce-4a87e7ced395)

Finally you can simply include the .h file in your project and flush it to your screen.

![5ad76504cf134ff9b00775188991b02](https://github.com/mxyxbb/lcd-image-to-mem-tool/assets/53026754/193a2053-c355-4e50-b539-5a182a21623d)
