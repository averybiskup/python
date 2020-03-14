import pygame, sys, math, time, random

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
    if dx_factor != 0:
        p1[0] += dx_factor
    elif dy_factor != 0:
        p1[1] += dy_factor
    else:
        return moveList

    moveList.append(p1[:])
    singleMove(p1, p2, moveList)
    return moveList



i = 40
MOVE_LIST = singleMove([-i,-i], [-i,i], []) + singleMove([-i,i], [i/4,i-30], []) + singleMove([i/4,i-30], [-i,i-30], []) + singleMove([-i,i-30], [i,-i], [])
# MOVE_LIST = singleMove([-i,-i], [-i,i], []) + singleMove([-i,10], [i-40,10], []) + singleMove([-i,i], [i-40,i], [])
CURRENT_POINT = 0


def random_list():
    list = []

    for i in range(100000):
        list.append(random.sample(range(-50, 50), 2))
    return list


def parabola(h, k, a):
    list = []

    for i in range(-500,500):
        li = [i, (a*((i-h))**2) + k]
        list.append(li)

    return list


# MOVE_LIST = random_list()
# print(MOVE_LIST)



WIDTH = 600
HEIGHT = 600
WHITE = (255,255,255)
RED = (255, 0, 0)
BLOCK_DIMENSION = WIDTH/100
SPEED = 5


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_running = True

def draw_point(point):
    x = point[0] * BLOCK_DIMENSION
    y = point[1] * BLOCK_DIMENSION
    abs_x = WIDTH/2
    abs_y = HEIGHT/2

    # pygame.draw.circle(screen, RED, (int(x + abs_x), int(abs_y - y)), 9)
    pygame.draw.circle(screen, (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)), (int(x + abs_x), int(abs_y - y)), 9)

def draw_grid():
    for i in range(0, 100):
        i *= BLOCK_DIMENSION
        pygame.draw.lines(screen, (0,0,0), False, [(0,i), (WIDTH,i)], 1)
        pygame.draw.lines(screen, (0,0,0), False, [(i,0), (i,HEIGHT)], 1)

def draw(point_list):
    for i in range(0, len(point_list)):
        draw_point(point_list[i])

def brush(list):
    for i in range(0, len(list)-5):
        # pygame.draw.circle(screen, RED, (list[i][0], list[i][1]), 1)
        pygame.draw.lines(screen, (0,0,0), False, [(list[i][0],list[i][1]), (list[i+1][0],list[i+1][1])], 1)
        # pygame.draw.lines(screen, (0,0,0), False, [(list[i][0],list[i][1]), (list[i+5][0],list[i+5][1])], 1)

DRAWEVENT = pygame.USEREVENT

pygame.time.set_timer(DRAWEVENT, 1)

point_list = []


while game_running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_running = False

        if pygame.event.get(DRAWEVENT):
            CURRENT_POINT += SPEED

        # if event.type == pygame.MOUSEMOTION:
            # print('mousedown')
            # mouse_x = pygame.mouse.get_pos()[0]
            # mouse_y = pygame.mouse.get_pos()[1]
        point_list.append([pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]])


        # pygame.draw.circle(screen, RED, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 100)



        screen.fill((250,250,250))
        # draw_grid()
        # draw_point([0,0])
        # pygame.draw.circle(screen, RED, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 100)
        # if event.type == pygame.KEYDOWN:
        brush(point_list)
        # draw(point_list)
        # draw(MOVE_LIST[0:CURRENT_POINT])


        pygame.display.flip()

pygame.quit()
sys.exit()
