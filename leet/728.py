def selfDividingNumbers(left, right):
    fit = []
    for i in range(left, right + 1):
        li = list(filter(lambda a: int(a) != 0 and i % int(a) == 0, list(str(i))))

        if len(li) == len(str(i)):
            fit.append(i)

    return fit

print(selfDividingNumbers(1, 22))
print(selfDividingNumbers(47, 85))
print(selfDividingNumbers(66, 708))

def test(i):
    li = list(map(lambda a: int(a), list(str(i))))
    li = list(filter(lambda a: a != 0 and i % a == 0, li))
    print(li)
# test(93)
