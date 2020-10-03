# this program is for checking how similar two strings are quickly.

s1 = input('>')
s2 = 'banana'


d1 = {}
d = {}

for n in s2:
    d1[n] = 1

for i in s1 + s2:
    d[i] = 1


l = len(d.keys())
l2 = len(d1.keys())


sim = round(float(l)/float(l2) * 100) 

print('{} | {} = {}'.format(s1, s2, sim))

