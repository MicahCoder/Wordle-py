from Board import Board
from Dictionary import Dictionary
from Board import LetterList
from time import sleep
def ClearScreen():
    print("\033[2J")
    print("\033[H")

dict = Dictionary()
board = Board(dict.getRandomWord(), dict)
letterList = LetterList()
def playTurn(board):
    ClearScreen()
    print(board)
    print(letterList)
    print("Write quit to exit game")
    guess = input("Enter your guess: ").upper()
    if guess == "quit":
        print("Exiting game.")
        return False
    if not dict.checkWord(guess):
        print("Invalid word, try again.")
        sleep(1.5)
        return True
    board.guessNext(guess)
    return True
while(not board.isComplete()):
    if not playTurn(board):
        break


