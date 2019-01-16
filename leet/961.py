a = [1,2,3,3]
b = [5,1,5,2,5,3,5,4]

def test(b):
    for i in b:
        l = list(filter(lambda x: x == i, b))
        if len(l) == len(b)/2:
            return l[0]

print(test(a))
