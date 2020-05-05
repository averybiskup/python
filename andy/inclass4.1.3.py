n = input('Filename: ')

f = open(n + '.txt', 'r')

lines = f.read().split('\n')[0:-1]

n = 1
for i in lines:
    print('{}: {}'.format(n, i))
    n += 1
