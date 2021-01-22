# attempts to change an image into something that looks like a sketch

from PIL import Image
import pyautogui
import time

# img = Image.open('small-world.jpg').convert('1')
img = Image.open('greyscale2.png')
# img.save('greyscale2.png')
# img.show()
#
x = float(img.size[0])
y = float(img.size[1])

pixels = img.load()

#
# for i in range(1, int(x)):
#     for j in range(1, int(y)):
#         if pixels[i-1, j] == 0 and pixels[i, j] == 255:
#             # print('replaced')
#             pixels[i-1, j] = 255
#
# # img.convert('RGBA')
#
# img.save('greyscale2.png')
# img.show()
#

print('Set Location')
time.sleep(5)

start_x = pyautogui.position()[0]
start_y = pyautogui.position()[1]


step_size = 2

for l in range(0, int(x/step_size)):
    for i in range(0, int(y/step_size)):

        if pixels[l,i] == 0:
            new_x = int(l*step_size)
            new_y = int(i*step_size)
            pyautogui.click(start_x + new_x, start_y + new_y)
            pyautogui.moveTo(start_x + new_x, start_y + new_y, duration = 0)
