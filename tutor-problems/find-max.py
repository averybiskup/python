# Use map with a lambda function that takes two parameters
# Find the largest number in the list

# I don't think it's possible to use map for this task
# Just going to use a for loop

l = list(range(0,11))

a = l[0]

getMax = lambda x, y: y if y >= x else x
for i in l:
    a = getMax(i, a)
# t = map(getMax(a), l)
# a = getMax(l[5], a)
print(a)
# for i in l:
#     a = getMax(i, a)

# maxList = [getMax(a, i) for i in l]
# print(a)
# print(maxList)
