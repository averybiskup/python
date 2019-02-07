def judgeCircle1(moves):
    directions = {
        'L': -1,
        'R': 1,
        'U': 1,
        'D': -1
    }

    y = 0
    x = 0
    for i in moves:
        if i == "L" or i == "R":
            x += directions[i]
        else:
            y += directions[i]

    return x == 0 and y == 0



def judgeCircle2(moves):
    d = {
        'L': 0,
        'R': 0,
        'U': 0,
        'D': 0
    }

    for i in moves:
        d[i] += 1

    return d['L'] - d['R'] == 0 and d['U'] - d['D'] == 0


def judgeCircle3(moves):
    return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

print(judgeCircle3('RRDD'))
