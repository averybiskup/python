def hammingDistance(x, y):
        b_x = "{0:b}".format(x)
        b_y = "{0:b}".format(y)

        print(b_x)
        print(b_y)

        a_x = (len(b_y) * "0") + b_x
        a_y = (len(b_x) * "0") + b_y

        count = 0
        for i in range(len(a_x)):
            if (a_x[i] != a_y[i]):
                count += 1

        return count

print(hammingDistance(653, 3984))
