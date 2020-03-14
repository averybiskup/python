from PIL import Image, ImageMorph, ImagePalette
import numpy as np

img1 = Image.open('flower.jpg').convert('RGBA')
img2 = Image.open('deep_fried.jpg').convert('RGBA')

# color = list(img2.getpixel((50,50)))[0:3]


color = [255,255,255]

img2 = img2.convert('RGBA')
data = np.array(img2)
rgb = data[:,:,:3]
# print(rgb)

def change(color):
    mask = np.all(rgb == color, axis = -1)
    data[mask] = [0,0,0,255]

# x = img2.size()
# y = img2.size()
# print(x, y)
# for i in range(x):
#     for n in range(y):
#         print(img2.getpixel((i,n)))
#
#
# i = 0
# p = 0
# for n in range(0, 5):
#     i += 10
#     print(i)
#     for k in range(0, 5):
#         p += 10
#         change(img2.getpixel((i, p))[0:3])
#
# new_im = Image.fromarray(data).convert('RGB')
# new_im.save('testing.jpg')
# new_im.show()

# white = (255,255,255)
# black = (0,0,0)
# for x in range(0, 2048, 100):
#     for y in range(0,1084):
#         img2.putpixel((x,y), black)
#         img2.putpixel((x-y,y), black)
# img2.show(command='fim')


img3 = Image.blend(img1, img2, 0.6).convert('RGB')
img3.save('image.jpg')
