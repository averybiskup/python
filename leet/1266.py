def getLength(p1, p2):
    len1 = p1[0] + p2[0]
    len2 = p1[1] + p2[1]
    return len1 + len2

def toNext(p1, p2, place):
    print(p1)
    number = -1 if p2[place] < 1 else 1
    
    if abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) >= 2:
        p1[0] += number
        p1[1] += number
        toNext(p1, p2, place)

    elif p1[place] != p2[place]:
        p1[place] += number
        toNext(p1, p2, place)
    else:
        return
        

def minTimeToVisitAllPoints(points):
    toNext(points[0], points[1], 1)
    toNext(points[0], points[1], 0)    
    print('--------')
    toNext(points[1], points[2], 1)
    toNext(points[1], points[2], 0)

minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])


