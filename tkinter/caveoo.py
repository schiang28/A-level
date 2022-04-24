# Bilbo's Amazing Adventure
import random
from tkinter import *


class Game:
    def __init__(self, data, root):
        self.startCave = None
        self.exitCave = None
        self.createCaves(data)
        self.player = Player("Player1")
        self.player.setCave(self.startCave)

        # construct the GUI
        self.root = root
        self.root.title("Cave Adventure")
        self.root.geometry("600x300")
        self.g = GUI(
            self.root, self
        )  # make it and pass a copy of the Game object to it!

    def createCaves(self, data):
        caves = dict()  # temp dict for creating initial set of caves
        fin = open(data, "r")
        caveData = fin.readlines()
        fin.close()
        # tidy up the input
        for i in range(len(caveData)):
            caveData[i] = caveData[i].strip().split(",")
            caves[caveData[i][0]] = Cave()
        self.startCave = caves[caveData[0][0]]
        self.exitCave = caves[caveData[len(caveData) - 1][0]]
        for line in caveData:
            print(line)
            caves[line[0]].setDesc(line[1])
            if line[2] != "0":
                caves[line[0]].setExit("N", caves[line[2]])
            if line[3] != "0":
                caves[line[0]].setExit("S", caves[line[3]])
            if line[4] != "0":
                caves[line[0]].setExit("W", caves[line[4]])
            if line[5] != "0":
                caves[line[0]].setExit("E", caves[line[5]])

    def play(self, direction):
        if self.player.alive() and self.player.getCave() != self.exitCave:
            self.player.takeTurn(direction)
            self.player.reportStatus()
        else:
            if self.player.alive():
                print("Conrgatulations you have found your way home.")
            else:
                print("You died!!!")
        self.g.updateExitButtons()
        self.g.location.set(self.player.cave.desc)


class Cave:
    def __init__(self):
        self.exits = dict({"N": None, "S": None, "W": None, "E": None})
        self.desc = ""
        self.monster = None
        self.treasure = None

        newMonster = random.randint(
            1, 64
        )  # 1 in 2 chance of a monster being in the cave
        if newMonster // 4 < 2:
            self.monster = Monster(newMonster)
        newArtefact = random.randint(
            1, 64
        )  # 1 in 2 chance of treasure being in the cave
        if newArtefact // 4 < 2:
            self.treasure = Artefact(newArtefact)

    def setExit(self, direction, cave):
        self.exits[direction] = cave

    def setDesc(self, description):
        self.desc = description

    def getMonster(self):
        return self.monster

    def getTreasure(self):
        return self.treasure


class Player:
    def __init__(self, name, strength=100):
        self.name = name
        self.strength = strength
        self.artefacts = list()
        self.cave = None

    def takeTurn(self, direction):

        self.cave = self.cave.exits[direction]

        monster = self.cave.getMonster()
        if monster != None:
            self.strength = self.strength - monster.getValue()
            print(
                "There is a {0} in the cave, you lose {1} strength points fighting it".format(
                    monster.getName(), monster.getValue()
                )
            )
        treasure = self.cave.getTreasure()
        if treasure != None:
            self.artefacts.append(treasure)
            print(
                "You have found a {0} worth {1} points".format(
                    treasure.getName(), treasure.getValue()
                )
            )

    def reportStatus(self):
        print(
            "{0} you have {1} strength points and the following treasure:".format(
                self.name, self.strength
            )
        )
        for artefact in self.artefacts:
            print("{0}: {1}".format(artefact.getName(), artefact.getValue()))

    def setCave(
        self, cave
    ):  # now used for entering a cave, must start a sequence of events!
        self.cave = cave

    def getCave(self):
        return self.cave

    def alive(self):
        if self.strength > 0:
            return True
        else:
            return False


class Artefact:
    typeNames = ("Sack of gold", "Bucket", "Magic potion")

    def __init__(self, artefactType):
        self.name = self.typeNames[artefactType % len(self.typeNames)]
        self.value = random.randint(1, 5) * 10
        print("art", artefactType)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value


class Monster:
    typeNames = ("Ogre", "Goblin", "Wizard")

    def __init__(self, monsterType):
        self.name = self.typeNames[monsterType % len(self.typeNames)]
        self.value = random.randint(1, 5) * 10
        print("monster", monsterType)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value


class GUI(Frame):
    def __init__(self, root, game):
        super(GUI, self).__init__(root)
        self.game = game
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        Label(self, text="Welcome " + self.game.player.name, padx=20, pady=10).grid(
            row=0, column=0, columnspan=5, sticky=NSEW
        )
        self.n = Button(
            self, text="North", command=lambda: self.game.play("N"), state=DISABLED
        )
        self.n.grid(row=1, column=2, sticky=W)

        self.e = Button(
            self, text="East", command=lambda: self.game.play("E"), state=DISABLED
        )
        self.e.grid(row=2, column=3, sticky=W)

        self.s = Button(
            self, text="South", command=lambda: self.game.play("S"), state=DISABLED
        )
        self.s.grid(row=3, column=2, sticky=W)

        self.w = Button(
            self, text="West", command=lambda: self.game.play("W"), state=DISABLED
        )
        self.w.grid(row=2, column=1, sticky=W)

        self.location = StringVar()
        Label(
            self,
            textvariable=self.location,
            relief=RAISED,
            padx=50,
            pady=50,
            wraplength=120,
            font=("Comic Sans", 13),
        ).grid(row=1, column=6, rowspan=5, sticky=NSEW)

        # set up initial button exits and description of current cave
        self.location.set(self.game.player.cave.desc)
        self.updateExitButtons()

    def updateExitButtons(self):
        self.n.config(state="disabled")
        self.s.config(state="disabled")
        self.e.config(state="disabled")
        self.w.config(state="disabled")
        for (
            direction
        ) in self.game.player.cave.exits.keys():  # for every exit in the current cave
            if direction == "N" and self.game.player.cave.exits[direction] != None:
                self.n.config(state="normal")
            if direction == "S" and self.game.player.cave.exits[direction] != None:
                self.s.config(state="normal")
            if direction == "E" and self.game.player.cave.exits[direction] != None:
                self.e.config(state="normal")
            if direction == "W" and self.game.player.cave.exits[direction] != None:
                self.w.config(state="normal")


root = Tk()
game = Game("data.csv", root)
root.mainloop()


# game.play()

