import time
import cursor

cursor.hide()

s = 'OLLEH'
f = 'HELLO'
t = 'We have a string, "Hello World", which we want to reverse:'
l = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's "

def backwards(s):
    n = len(s) + 3
    t = len(s)
    for i in range(0, len(s)+1):
        print('<', ' ' * n + s[:i], end='  >\r')
        t -=1
        n -= 1
        time.sleep(0.09)
    print('<   {}   '.format(s))

# backwards(t)

def decapitalize(s):
    for cur in range(0, len(s)):
        print(s[0:cur].lower() + s[cur:].upper(), end='\r')

        time.sleep(0.1)
    print(s.lower())

decapitalize(l)

cursor.show()
