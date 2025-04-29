GREEN = "\033[42m"
YELLOW = "\033[43m"
WHITE = "\033[47m"
RESET = "\033[0m"
class Board:
    def __init__(self, secretWord):
        self.index=0
        self.secretWord = secretWord
        self.board = ["","","","","",""]
    def __str__(self):
        out=''
        for row in self.board:
            out+= self.rowToPrint(row)+"\n"
        return out
    def rowToPrint(self,row):
        if len(row) == 0:
            return WHITE + "| | | | | |" + RESET
        # return GREEN + "|"+"|".join(row)+"|" + RESET
        return self.colorWord(row)
    def setRow(self,row,guess):
        self.board[row] = guess
    def getIndex(self):
        return self.index
    def guessNext(self,guess):
        if(self.index >= 6):
            raise Exception("No more guesses left")
        self.board[self.index] = guess
        self.index+= 1
    def getRow(self,row):
        return self.board[row]
    def colorWord(self,word):
        out = ["","","", "", "", ""]
        degreenedWord = list(word)
        #Green Codes First
        for i in range(len(word)):
            if word[i] == self.secretWord[i]:
                out[i] = GREEN + word[i]+"|" + RESET
                degreenedWord.remove(word[i])
        #Yellow
        print(degreenedWord)
        for i in range(len(word)):
            if word[i] in degreenedWord:
                out[i] = YELLOW + word[i]+"|" + RESET
                degreenedWord.remove(word[i])
        #Grey
        for i in range(len(word)):
            if len(out[i])==0:
                out[i] = WHITE + word[i]+"|" + RESET
        return "|" + "".join(out) + "|"
    