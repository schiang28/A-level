class PaperDispensor:
    def __init__(self, p):
        self.paper = p

    @property
    def paper(self):
        print("In getter")
        return self.__paper

    @paper.setter
    def paper(self, p):
        if p < 0:
            raise ValueError("Cannot set negative paper")
        self.__paper = p

    def take_paper(self):
        if self.paper == 0:
            raise Exception
        else:
            self.paper -= 1


n24_dispensor = PaperDispensor(2000)
n27_dispensor = PaperDispensor(-1)

a = "Hello"
b = len(a)  # Function
c = a.upper()  # Method

print(n24_dispensor.paper)
n24_dispensor.take_paper()
print(n24_dispensor.paper)