from Dictionary import Dictionary
from textwrap import wrap
GREEN = "\033[42m"
YELLOW = "\033[43m"
WHITE = "\033[47m"
BLACK = "\033[40m"
GREY = "\033[48;5;237m"
RESET = "\033[0m"
class LetterList:
    def __init__(self):
        self.letters = {"A":("white",(WHITE+ "A" + RESET)),
                        "B":("white",(WHITE+ "B" + RESET)),
                        "C":("white",(WHITE+ "C" + RESET)),
                        "D":("white",(WHITE+ "D" + RESET)),
                        "E":("white",(WHITE+ "E" + RESET)),
                        "F":("white",(WHITE+ "F" + RESET)),
                        "G":("white",(WHITE+ "G" + RESET)),
                        "H":("white",(WHITE+ "H" + RESET)),
                        "I":("white",(WHITE+ "I" + RESET)),
                        "J":("white",(WHITE+ "J" + RESET)),
                        "K":("white",(WHITE+ "K" + RESET)),
                        "L":("white",(WHITE+ "L" + RESET)),
                        "M":("white",(WHITE+ "M" + RESET)),
                        "N":("white",(WHITE+ "N" + RESET)),
                        "O":("white",(WHITE+ "O" + RESET)),
                        "P":("white",(WHITE+ "P" + RESET)),
                        "Q":("white",(WHITE+ "Q" + RESET)),
                        "R":("white",(WHITE+ "R" + RESET)),
                        "S":("white",(WHITE+ "S" + RESET)),
                        "T":("white",(WHITE+ "T" + RESET)),
                        "U":("white",(WHITE+ "U" + RESET)),
                        "V":("white",(WHITE+ "V" + RESET)),
                        "W":("white",(WHITE+ "W" + RESET)),
                        "X":("white",(WHITE+ "X" + RESET)),
                        "Y":("white",(WHITE+ "Y" + RESET)),
                        "Z":("white",(WHITE+  "Z"+RESET))}
        for letter in self.letters:
            letter
    def __str__(self):
        out =  GREY+" "*21 + "\n " + RESET
        letters = [i[1] for i in list(self.letters.values())]
        for i in range(len(letters)):
            out += letters[i] + GREY + " " + RESET
            if(i%10 == 9):
                out += "\n" + GREY + " " + RESET
        return out +GREY +"\n" + " "*13 + RESET
    def updateLetter(self,letter:str,color:str):
        if color == "green":
            self.letters[letter] = ("green",GREEN + letter + RESET)
        elif color == "yellow":
            self.letters[letter] = ("yellow",YELLOW + letter + RESET)
        elif color == "grey":
            self.letters[letter] = ("grey",GREY + letter + RESET)

class Board:
    def __init__(self, secretWord : str, dict : Dictionary, letterList : LetterList):
        self.index=0
        self.dict = dict
        self.letterList = letterList
        self.secretWord = secretWord
        self.board = ["","","","","",""]
    def __str__(self):
        out=''
        for row in self.board:
            out+= self.rowToPrint(row)+"\n"
        return out
    def rowToPrint(self,row: int):
        if len(row) == 0:
            return WHITE + "| | | | | |" + RESET
        # return GREEN + "|"+"|".join(row)+"|" + RESET
        return self.colorWord(row)
    def setRow(self,row:int,guess:str):
        self.board[row] = guess
    def getIndex(self):
        return self.index
    def guessNext(self,guess:str):
        if(self.index >= 6):
            raise Exception("No more guesses left")
        self.board[self.index] = guess
        self.index+= 1
    def getRow(self,row):
        return self.board[row]
    def colorWord(self,word):
        out = ["","","", "", "", ""]
        degreenedWord = list(self.secretWord)
        #Green Codes First
        for i in range(len(word)):
            if word[i] == self.secretWord[i]:
                out[i] = GREEN + word[i]+"|" + RESET
                self.letterList.updateLetter(word[i], "green")
                degreenedWord.remove(word[i])
        #Yellow
        for i in range(len(word)):
            if len(out[i])==0 and word[i] in degreenedWord:
                out[i] = YELLOW + word[i]+"|" + RESET
                self.letterList.updateLetter(word[i], "yellow")
                degreenedWord.remove(word[i])
        #Grey
        for i in range(len(word)):
            if len(out[i])==0:
                out[i] = GREY + word[i]+"|" + RESET
                self.letterList.updateLetter(word[i], "grey")
        return "|" + "".join(out)
    def isComplete(self):
        return self.index >= 6 or self.board[self.index-1] == self.secretWord