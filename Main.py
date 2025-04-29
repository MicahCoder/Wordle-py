from Board import Board
def clearScreen():
    print("\033[2J")
    print("\033[H")

board = Board("hello")
print(board)
clearScreen()
board.guessNext("helio")
board.guessNext("slate")
print(board)

