import os
import time

rows, columns = os.popen('stty size', 'r').read().split()


def lin(m, b):
    # y(x) = mx + b
    points = {}
    tpoints = {}
    for x in range(int(columns)):
        if (int(rows) - int(m*x + b)) <= 0:
            break
        # print((x+int(rows), int(rows) - int(m*x + b)))
        points[(x, int(rows) - int(m*x + b))] = True
        tpoints[(x, int(m*x + b))] = True

    return points


def square(x, y, w, h, maxw=rows, maxh=columns):
    points = {}
    for i in range(w):
        for l in range(h):
            points[(i + x, l + y)] = True
    return points

def add_shapes(s):
    s3 = {}
    for i in s:
        s3.update(i)
    return s3

def matrix(shape):
    os.system('clear')
    for i in range(int(rows) - 1):
        for n in range(int(columns)):
            if (n, i) in shape:
                print('*', end='')
            else:
                print(' ', end='')

s = [lin(i/10, 0) for i in range(0, 100, 1)]
