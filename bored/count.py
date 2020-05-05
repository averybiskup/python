f = open('numbers.txt', 'r')

count = 0
for i in f.read().split('\n'):
    # print(float(i))
    if len(i):

        count += float(i)
print(count)
