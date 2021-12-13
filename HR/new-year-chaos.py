#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def sub_tree(num, root):
    #print(root)
    if num == root['value']:
        return root
    elif num > root['value']:
        root = sub_tree(num, root['right'])
    else:
        root = sub_tree(num, root['left'])
    return root
            
def count_children(root, count):
    if 'left' in root and 'right' in root and len(root['left']) + len(root['right']) >= 0:
        count = 1
    
    if 'left' in root and len(root['left'].keys()) > 0:
        count += count_children(root['left'], count)
    if 'right' in root and len(root['right'].keys()) > 0:
        count += count_children(root['right'], count)
    
    return count

def add_node(num, root):
    if len(root.keys()) > 0:
        if num > root['value']: 
            root['right'] = add_node(num, root['right'])
        else:
            root['left'] = add_node(num, root['left'])
            if 'value' in root['right']:
                root['right'] = add_node(num, root['right'])
            
            
    else:
        root = {'value': num, 'left': {}, 'right': {}}
        
    return root
                

def minimumBribes(q):
    bc = {}
    count = 0
    chaos = False
    
    for num in q:
        bc = add_node(num, bc)
    
    total = 0
    for num in q:
        c = count_children(sub_tree(num, bc)['left'], count)
        if c >= 3:
            chaos = True
        total += c
        
    if chaos:
        print('Too chaotic')
    else:
        print(total)
        
    
    
    
if __name__ == '__main__':
    with open('data.txt', 'r') as f:

        r = f.read()

        l = list(map(int, r.rstrip().split()))
        minimumBribes(l)
        # for i in range(r.split(' ')):
            # print(r)
            # n = int(input().strip())

            # q = list(map(int, input().rstrip().split()))

            # minimumBribes(q)

