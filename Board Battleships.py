import time
def Print_Board():
    for row in range(0,len(board)):
        for column in range (0,len(board[row])):
            print(board[row][column], end='')
        print()
board = [['#','#','#','#'],['#','#','#','#'],['#','#','#','#'],['#','#','#','#']]
Print_Board()
