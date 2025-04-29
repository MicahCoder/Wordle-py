from Board import Board
def ClearScreen():
    print("\033[2J")

board = Board("hello")
print(board)

board.guessNext("helio")
board.guessNext("slate")
print(board)

