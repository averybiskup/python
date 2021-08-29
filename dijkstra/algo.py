import copy

g = {
    'a': {
        'neighbors': [('b', 3), ('h', 4), ('e', 5)],
        'visited': False,
        'value': float('inf')
        },
    'b': {
        'neighbors': [('a', 3), ('e', 5), ('c', 2), ('f', 7)],
        'visited': False,
        'value': float('inf')
        },
    'c': {
        'neighbors': [('d', 3), ('g', 6), ('b', 2), ('f', 2)],
        'visited': False,
        'value': float('inf')
        }, 
    'd': {
        'neighbors': [('c', 3), ('g', 7), ('z', 2)],
        'visited': False,
        'value': float('inf')
        },
    'e': {
        'neighbors': [('a', 5), ('b', 5), ('h', 7), ('f', 4)],
        'visited': False,
        'value': float('inf')
        },
    'f': {
        'neighbors': [('e', 4), ('b', 7), ('h', 5), ('i', 4), ('j', 3), ('g', 4), ('c', 2)],
        'visited': False,
        'value': float('inf')
        },
    'g': {
        'neighbors': [('c', 6), ('j', 4), ('d', 7), ('f', 4), ('z', 6)],
        'visited': False,
        'value': float('inf')
        },
    'h': {
        'neighbors': [('a', 4), ('e', 7), ('f', 5), ('i', 2)],
        'visited': False,
        'value': float('inf')
        },
    'i': {
        'neighbors': [('h', 2), ('j', 6), ('f', 4)],
        'visited': False,
        'value': float('inf')
        },
    'j': {
        'neighbors': [('i', 6), ('f', 3), ('g', 4), ('z', 5)],
        'visited': False,
        'value': float('inf')
        },
    'z': {
        'neighbors': [('j', 5), ('g', 6), ('d', 2)],
        'visited': False,
        'value': float('inf')
        },
    }

# Start vertex, end vertex, and previous vertex's value
def d(s, e, value):

    # Base case
    if (s == e):
        return
    
    # get neighbors
    neighbors = g[s]['neighbors']

    # We've visited this vertex
    g[s]['visited'] = True

    # Visiting all neighbors
    for n in neighbors:
        if value + n[1] < g[n[0]]['value']:
            g[n[0]]['value'] = value + n[1]

    # Recursing over neighbors
    for n in neighbors:
        if (not g[n[0]]['visited']):
            d(n[0], e, g[n[0]]['value'])


start = 'a'
end = 'z'

g[start]['value'] = 0

d(start, end, 0)

length = g[end]['value']

COMMENTS
given proper data such as that to the right, this algorithm works,
using python.

I could not figure out how to give the path with code, but the idea
is to keep track of the last vertex, and keep updating it with the 
new ones as long as the path from that one to the first is not greater.

keeping a list of these updates, would give you the path






