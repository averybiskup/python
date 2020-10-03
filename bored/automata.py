# RULES

# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


# <2 dies
# 2-3 lives
# >3 dies
# 3 born


class Cell:

    def __init__(self, x, y, live):
        self.x = x # x coord
        self.y = y # y coord       
        self.live = True # alive (True) or dead (False)
        self.n = 0 # neighbor count

    def is_neighbor(self, x, y):
        if abs(x - self.x) + abs(y - self.y) <= 2:
            return True
        
        return False

    def add_n(self):



t = Cell(0, 0, True)

        
