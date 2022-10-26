import random
from collections import defaultdict

def run_test():
    s1 = random.randint(1,6)
    s2 = random.randint(1,6)
    s3 = random.randint(1,6)

    return max(s1, s2, s3) - min(s1, s2, s3)

d = defaultdict(int)
num = 1000000
for i in range(num):
    d[run_test()] += 1

print(d)
count = 0
for key in d.keys():
    print(key, d[key] / num)
    count += d[key] / num
print(count)

