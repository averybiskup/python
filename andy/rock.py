import random

"""
    The play function plays the game with a while loop, and queries the user for rock paper or scissors.

    EXAMPLE OUTPUT:
    Move: scissors
    Computer wins! Rock breaks Scissors!
    ------
    Move: rocks
    Tie with rock
    ------
    Move: ROCK
    You wins! Rock breaks Scissors
    ------
    Move: Paper
    You win! Paper covers Rock!
    ------
    Move: papers
    You win! Paper covers Rock!
    ------
    Move: q
"""

def play():
    moves = ['rock', 'paper', 'scissor']

    while True:
        move = input('Move: ').lower()
        if move[-1] == 's':
            move = move[0:-1]

        cmove = random.choice(moves)

        if move == cmove:
            print('Tie with {}'.format(move))
        elif move == 'scissor' and cmove == 'rock':
            print('Computer wins! Rock breaks Scissors!')
        elif move == 'rock' and cmove == 'scissor':
            print('You wins! Rock breaks Scissors')
        elif move == 'paper' and cmove == 'scissor':
            print('Computer wins! Scissors cut Paper!')
        elif move == 'scissor' and cmove == 'paper':
            print('You wins! Scissors cut Paper!')
        elif move == 'rock' and cmove == 'paper':
            print('Computer wins! Paper covers Rock!')
        elif move == 'paper' and cmove == 'rock':
            print('You win! Paper covers Rock!')
        else:
            break
        print('------')

def main():
    play()

if __name__ == '__main__':
    main()
