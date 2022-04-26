class State:
    def __init__(self, name):
        self.name = name
        self._rules = {}

    def addRule(self, match, newState):
        self._rules[match] = newState

    def getNextState(self, match):
        return self._rules[match]


class FSM:
    def __init__(self, inputTape):
        self.curr = states["S0"]
        for i in inputTape:
            self.doNextTransition(i)

        if self.curr.name[0] == "A":
            print("accepted")
        else:
            print("rejected")

    def doNextTransition(self, i):
        n = self.curr.getNextState(i)
        print(self.curr.name + "->" + n.name, i)
        self.curr = n


with open("fsm.txt", "r") as f:
    rules = [i.split() for i in f.read().splitlines()]

with open("inp.txt", "r") as f:
    inputs = f.read().splitlines()

states = {s: State(s) for s in set([i[0] for i in rules])}
[states[r[0]].addRule(r[1], states[r[2]]) for r in rules]

for i in inputs:
    machine = FSM(i)
