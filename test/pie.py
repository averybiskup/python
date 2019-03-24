t = [1/float(n) for n in range(1,100000) if n % 2 == 1]

for i, l in enumerate(t):
    # print(i, l)
    if (i % 2 == 1):
        t[i] = (-1 * t[i])
print(sum(t) * 4)
