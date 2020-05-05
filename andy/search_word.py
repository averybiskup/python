word = input('Word: ')
f = open('test_search.txt', 'r')

lines = f.read().split('\n')

line_count = 0
count = 0
for i in lines:
    if word in i.split(' '):
        for w in i.split(' '):
            if w == word:
                count += 1
        print(word)
        line_count += 1

print('Times found: {}'.format(count))
print('Lines: {}'.format(line_count))
