# POINT_LIST = []
#
# def getLength(p1, p2):
#     len1 = p1[0] + p2[0]
#     len2 = p1[1] + p2[1]
#     return len1 + len2
#
# def toNext(p1, p2, place):
#     print(p1)
#     number = -1 if p2[place] < 1 else 1
#
#     # Diagonal Movement
#     if abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) >= 2:
#
#         p1[0] += number
#         p1[1] += number
#         toNext(p1, p2, place)
#
#
#     # Linear Movement
#     elif p1[place] != p2[place]:
#         p1[place] += number
#         toNext(p1, p2, place)
#
#     else:
#         return
#
# def minTimeToVisitAllPoints(points):
#     toNext(points[0], points[1], 1)
#     toNext(points[0], points[1], 0)
#     print('--------')
#     toNext(points[1], points[2], 1)
#     toNext(points[1], points[2], 0)

# minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
# print(POINT_LIST)

# list = []

def singleMove(p1, p2, moveList = []):

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    dx_factor = int(dx/abs(dx)) if dx != 0 else 0
    dy_factor = int(dy/abs(dy)) if dy != 0 else 0

    main_factor = dx_factor if dx_factor == dy_factor else 0

    overlap = abs(dx) >= 1 and abs(dy) >= 1 and dx_factor == dy_factor

    if overlap:
        p1[0] += main_factor
        p1[1] += main_factor
    elif dx_factor != 0:
        p1[0] += dx_factor
    elif dy_factor != 0:
        p1[1] += dy_factor
    else:
        return moveList

    moveList.append(p1[:])
    singleMove(p1, p2, moveList)
    return moveList


print(singleMove([4,-3], [10,10]))
# print(list)
