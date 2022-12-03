def c(a, b, x, y):
    print("\n")
    print(a, b, x, y)
    flag = 0
    if x > a + b:
        print("S2, S3")
        flag = -1
    elif y > a + b:
        print("S4, S5")
        flag = 1

    if (a + x) > (flag * (b + y)):
        print("S6, S7")
        flag = 1
    elif (a + y) > (2 * flag * x):
        print("S8, S9")
        flag = -1

    return flag

print("S1, S2, S3, S4, S5, S6, S7, S8, S9, S10")

'''
print(0, c(1, 1, -1, -1)) # 1
print(-1, c(0, -1, 1, -2)) # 2, 3
print(1, c(0, 1, 1, 2)) # S4, S5
print(1, c(1, 0, 0, 0)) # S6, S7
print(-1, c(2, -1, -2, -1)) # S8, S9
'''

print(1, c(0, 0, 1, 0)) # S2, S3, S6, S7
#print(-1, c(0, 0, 1, -1)) # S2, S3, S8, S9

#print(1, c(2, -1, 0, 2)) # S4, S5, S6, S7
print(-1, c(0, 0, 0, 1)) # S4, S5, S8, S9


#y < a + b
#b + y > a + x
#a + y < 2 * x


#print(1, c(0, 1, 2, 0))

