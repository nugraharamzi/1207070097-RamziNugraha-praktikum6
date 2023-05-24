#MENGIMPORT LIBRARY
import numpy as np
import imageio
import cv2
import matplotlib.pyplot as plt
#membaca gambar
img = plt.imread("pin.jpg")
#memasukan resolusi dan tipe gambar
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
img_type = img.dtype
#Membuat variabel dengan resolusi dan tipe yang sama seperti gambar
img_flip_horizontal = np.zeros(img.shape, img_type)
img_flip_vertical = np.zeros(img.shape, img_type)
#Membalik gambar secara horizontal dengan perulangan for
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]
#Membalik gambar secara vertikal dengan perulangan for
for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]
#Menampilkan hasil balik gambar horizontal
plt.imshow(img_flip_horizontal)
plt.title("Flip Horizontal")
plt.show()
#Menampilkan hasil balik gambar vertikal
plt.imshow(img_flip_vertical)
plt.title("Flip Vertical")
plt.show()