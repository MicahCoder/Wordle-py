from Board import Board
from Dictionary import Dictionary
def ClearScreen():
    print("\033[2J")
    print("\033[H")

dict = Dictionary()
board = Board(dict.getRandomWord(), dict)
def playTurn(board):
    ClearScreen()
    print(board)
    guess = input("Enter your guess: ")
    if not dict.checkWord(guess):
        print("Invalid word, try again.")
        return False
    board.guessNext(guess)
    return True
while(not board.isComplete()):
    playTurn(board)
# print(board)

# board.guessNext("helio")
# board.guessNext("slate")
# print(board)

