from Board import Board
from Dictionary import Dictionary
from Board import LetterList
from time import sleep

dict = Dictionary()

def ClearScreen():
    print("\033[2J")
    print("\033[H")
def playTurn(board, letterList):
    ClearScreen()
    print(board)
    print(letterList)
    print("Write quit to exit game")
    guess = input("Enter your guess: ").upper()
    if guess == "QUIT":
        print("Exiting game.")
        return False
    if not dict.checkWord(guess):
        print("Invalid word, try again.")
        sleep(1)
        return True
    board.guessNext(guess)
    return True
def playGame():
    letterList = LetterList()
    board = Board(dict.getRandomWord(), dict,letterList)
    while(not board.isComplete()):
        if not playTurn(board,letterList):
            break
    ClearScreen()
    print(board)
    print("The secret word was:"+ board.secretWord)
    print("YOU WIN!" if board.winState() else "YOU LOSE!")
    print("Press enter to play again, write quit to exit")
while True:
    playGame()
    if input().lower() == "quit":
        break
    ClearScreen()

