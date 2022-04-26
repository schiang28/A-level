class State:
    def __init__(self, name):
        self.name = name
        self._rules = {}

    def addRule(self, match, newState):
        self._rules[match] = newState

    def getNextState(self, match):
        return self._rules[match]

    ...


class FSM:
    def __init__(self, transitionRules, inputTape):
        self.transitionRules = transitionRules
        self.inputTape = inputTape

    def doNextTransition(self, p):
        return State(self.getNextState(self.inputTape[p]))

    currentState = State("S0")
    # for i in self.inputTape:


# add states first
# rules key = "a": State(a3)

with open("fsm.txt") as f:
    fsmDef = [i.split() for i in f.read().splitlines()]

with open("inp.txt") as f:
    fsmInp = f.read().splitlines()

states = []
for s in range(0, len(fsmDef), 2):
    state = State(fsmDef[s][0])
    states.append(state)

for s in range(len(states)):
    state.addRule(fsmDef[s * 2][1], State(fsmDef[s * 2][2]))
    state.addRule(fsmDef[s * 2 + 1][1], State(fsmDef[s * 2 + 1][2]))

print(states)

for i in fsmInp:
    machine = FSM(fsmDef, fsmInp)
