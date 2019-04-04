try:
    from PIL import Image
except:
    import Image
import pytesseract
import os

s = (str(pytesseract.image_to_string(Image.open('test6.jpg'))))
# print(s)
s = s.split('>', 1)[1].replace('\n', ' ')
s = s.split('>')
# print(s)
for i in s:
    print(i)
    say = "say {}".format(i.replace("'", ''))
    os.system(say)
