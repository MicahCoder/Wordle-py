import random

class Dictionary:
    def __init__(self):
        self.legalWords = None
        self.wordleWords = None
    def checkWord(self, word:str):
        if(self.legalWords == None):
             self.legalWords = open("assets/5LetterDict.txt","r").read().splitlines()
        return word.lower() in self.legalWords
    def getRandomWord(self):
        if(self.wordleWords == None):
            self.wordleWords = open("assets/wordleWords.txt","r").read().splitlines()
        return random.choice(self.wordleWords).upper()