import os




class Board:


    def __init__(self, size_x, size_y):
        self.cells = {}
        self.size_x = size_x
        self.size_y = size_y
        self.tick = 0

    def create_board(self):
        for x in range(self.size_x * -1, self.size_x):
            for y in range(self.size_y * -1, self.size_y):
                self.cells[(x, y)] = False
   
    def put(self, coord):
        self.cells[coord] = True

    def n(self, cell, p=False):
        count = 0

        for x in range(cell[0] - 1, cell[0] + 2):

            for y in range(cell[1] - 1, cell[1] + 2):
                if p:
                    print(x, y, self.cells[(x, y)])
                if (x, y) in self.cells:
                    if self.cells[(x, y)] == True and (x, y) != cell:
                        count += 1

        return count
    
    def next_tick(self):
        self.tick += 1

        old_cells = self.cells.copy()


        for cell, live in self.cells.items():

            neighbors = self.n(cell)

            if neighbors == 2:
                pass

            elif neighbors > 3 and self.cells[cell] == True:
                old_cells[cell] = False
                #print(cell, ' | died | ', self.n(cell))
                
            elif neighbors < 2 and self.cells[cell] == True:
                old_cells[cell] = False
                #print(cell, ' | died | ', self.n(cell))

            elif neighbors == 3 and self.cells[cell] == False:
                old_cells[cell] = True
                #print(cell, ' | born')

            elif neighbors == 3:
                pass
       
        self.cells = old_cells

        self.print_board()

    def print_board(self):
        count = 0

        print(self.tick)

        for y in range(self.size_y - 1, self.size_y * -1, -1):
            for x in range(self.size_x * -1, self.size_x):
                if (x, y) in self.cells:
                    if self.cells[(x, y)] and x == 0 and y == 0:
                        print('C', end=" ")
                    elif self.cells[(x, y)]:
                        print('O', end=" ")
                    else:
                        print('.', end=" ")
                else:
                    print('.', end="")

                count += 1

                if count == self.size_x * 2:
                    print('')
                    count = 0
                
b = Board(30,30)

b.create_board()


b.put((0,0))
b.put((1,1))
b.put((1,0))
b.put((-1, -1))
b.put((-1, 0))
b.put((2, 2))
b.put((2,1)) 



b.print_board() 


while True:
    i = input('')
    if i:
        break
    
    os.system('clear')
    b.next_tick()
