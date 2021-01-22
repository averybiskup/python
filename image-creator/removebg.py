# attempts to remove the background by grabbing some color to keep


from PIL import Image, ImageMorph, ImagePalette
import numpy as np

img = Image.open('flower.jpg').convert('RGBA')

x = img.size[0]
y = img.size[1]

data = np.array(img)
rgb = data[:,:,:3]

def near_color(col1, col2):
    first = abs(col1[0] - col2[0])
    second = abs(col1[1] - col2[1])
    third = abs(col1[2] - col2[2])
    return (first + second + third) <= 130

blue = (86,128,156)
black = (0,0,0,255)
yellow = (255,213,0, 255)
pink = (250, 108, 196, 255)
gray = (130,130,130)

out_im = Image.new('RGB', (x,y), gray)


def change(color):

    mask = np.all(near_color(rgb, color), axis = -1)
    data[mask] = [0,0,0,255]


# img.getpixel((1571, 1032))
pixels = img.load()
new_pixels = out_im.load()
for i in range(x-1):
    for l in range(y-1):
        # print(pixels[i, 0])
        if near_color(pixels[i, l], pink):
                print(i, l)
                # pixels[i, l] = black
                new_pixels[i, l] = yellow
                pixels[i, l] = yellow

new_im = img.convert('RGB')
new_im.save('done.jpg')
new_im.show()

out_im.save('deep_fried.jpg')
out_im.show()


# for i in range(5):
#     # print(i)
#     for j in range(5):
#         change(img.getpixel((j, i))[0:3])
#
# new_im = Image.fromarray(data).convert('RGB')
# new_im.save('done.jpg')
# new_im.show()
