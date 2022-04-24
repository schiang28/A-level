from tkinter import *

# LIBRARIES
import random

# CONSTANTS
NUM_GUESSES = 6
WORDS_FILE = "words.txt"

# GLOBAL VARS
game = False
gameWord = ""
resultLabels = []
answerLabel = None
entries = []
entryTexts = []
guesses = 0


def loadWords():
    # return list of words from text file
    # note they will all end in \n but ignore that for now
    # local vars
    file = None
    lines = []

    file = open(WORDS_FILE, "r")
    lines = file.readlines()

    return lines


def selectWord(wordList):
    # pick a random word and return it
    # local vars
    choice = 0
    selectedWord = ""

    choice = random.randint(0, len(wordList) - 1)
    selectedWord = wordList[choice].strip()
    return selectedWord


def checkValidWord(word, wordlist):
    # check if 5 letters long and in the list of valid words
    if len(word) == 5 and (word + "\n") in wordlist:
        return True
    else:
        return False


def checkGuess(event):
    # evaluate and update feedback textboxes
    # # N = wrong, S = somewhere but wrong location, Y = correct!

    global guesses
    wordGuess = event.widget.get()

    if checkValidWord(wordGuess, words) == False:
        entryTexts[guesses].set("")
    else:
        if event.widget.cget("state") == "normal":
            event.widget.config(state="disabled")
            guesses += 1
            if guesses < NUM_GUESSES:
                entries[guesses].config(state="normal")

        foundWrong = False
        for index in range(0, len(wordGuess)):
            if wordGuess[index] == selectedWord[index]:
                resultLabels[index].config(text="Y")
            elif wordGuess[index] in selectedWord:
                resultLabels[index].config(text="S")
                foundWrong = True
            else:
                resultLabels[index].config(text="N")
                foundWrong = True

        if guesses == NUM_GUESSES or not foundWrong:
            answerLabel.config(text=selectedWord)


def makeGuessBoxes(root):
    entries = []
    entryTexts = []
    for index in range(NUM_GUESSES):
        row = Frame(root)
        lab = Label(row, width=22, text="Guess " + str(index + 1), anchor="w")
        entryText = StringVar()
        ent = Entry(row, textvariable=entryText)
        ent.config(state="disabled")
        ent.config(justify="center")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append(ent)
        entryTexts.append(entryText)
        entries[0].config(state="normal")
    return entries, entryTexts


def makeResultBoxes(root):
    labels = []
    resultRow = Frame(root)
    resultRow.pack(side=TOP, fill=X, padx=5, pady=5)
    resultLab = Label(resultRow, width=10, text="Result:", anchor="w")
    resultLab.pack(side=LEFT)
    for _ in range(5):
        resultLab = Label(resultRow, width=1, text="", anchor="w")
        resultLab.config(bg="white")
        resultLab.pack(side=LEFT, padx=25)
        labels.append(resultLab)
    answerRow = Frame(root)
    answerRow.pack(side=TOP, fill=X, padx=5, pady=5)
    answerLab = Label(answerRow, width=10, text="Answer:", anchor="w")
    answerLab.pack(side=LEFT)
    answer = Label(answerRow, width=10, text="", anchor="w")
    answer.config(bg="white")
    answer.pack(side=LEFT, padx=25)
    return labels, answer


###################
# MAIN
##################

# setup
words = loadWords()
selectedWord = selectWord(words)

# create graphical window
root = Tk()
entries, entryTexts = makeGuessBoxes(root)
resultLabels, answerLabel = makeResultBoxes(root)

root.bind("<Return>", (lambda event, e=entries: checkGuess(event)))
root.bind("<1>", (lambda event, e=entries: checkGuess(event)))
root.mainloop()
