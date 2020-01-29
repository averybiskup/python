import pygame, sys, math, time

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# pygame.display.update()
#
# red = (255, 0, 0)
#
# screen.fill(red)

WHITE = (255,255,255)
RED = (255, 0, 0)

# Game Loop

game_running = True

def draw_point(x, y):
    x *= 25
    y *= 25
    abs_x = WIDTH/2
    abs_y = HEIGHT/2

    pygame.draw.circle(screen, RED, (int(x + abs_x), int(y + abs_y)), 5)

def draw_grid():
    for i in range(0, 100):
        i *= 25
        pygame.draw.lines(screen, WHITE, False, [(0,i), (WIDTH,i)], 1)
        pygame.draw.lines(screen, WHITE, False, [(i,0), (i,HEIGHT)], 1)

while game_running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_running = False

        screen.fill((0,100,150))
        draw_grid()
        draw_point(0, 0)
        draw_point(1, 0)
        draw_point(0, 1)
        draw_point(0, -1)
        draw_point(-1, 0)
        # pygame.draw.lines(screen, WHITE, False, [(0,0), (100,100)], 1)

        pygame.display.update()

pygame.quit()
sys.exit()



# def getLength(p1, p2):
#     len1 = p1[0] + p2[0]
#     len2 = p1[1] + p2[1]
#     return len1 + len2
#
# def toNext(p1, p2, place):
#     print(p1)
#     number = -1 if p2[place] < 1 else 1
#
#     if abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) >= 2:
#         p1[0] += number
#         p1[1] += number
#         toNext(p1, p2, place)
#
#     elif p1[place] != p2[place]:
#         p1[place] += number
#         toNext(p1, p2, place)
#     else:
#         return
#
#
# def minTimeToVisitAllPoints(points):
#     toNext(points[0], points[1], 1)
#     toNext(points[0], points[1], 0)
#     print('--------')
#     toNext(points[1], points[2], 1)
#     toNext(points[1], points[2], 0)
#
# minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
