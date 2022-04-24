class Animal:
    def __init__(self):
        self.__coldBlooded = False
        self.__skinType = None
        self.__tail = False
        self.__legs = 0
        self.__arms = 0
        self.__wings = 0

    def move(self):
        raise NotImplementedError()

    def eat(self):
        raise NotImplementedError()

    def birth(self):
        raise NotImplementedError()

    def hibernate(self):
        raise NotImplementedError()

    def getInfo(self):
        raise NotImplementedError()

    def getInfo(self):
        if self.__coldBlooded:
            print("This animal is cold-blooded")
        else:
            print("This animal is warm-blooded")
        if self.__skinType != None:
            print(f"This animal is covered in {self.__skinType}")
        if self.__tail:
            print("This animal has a tail")
        if self.__legs > 0:
            print(f"This animal has {self.__legs} legs")
        if self.__arms > 0:
            print(f"This animal has {self.__arms} arms")
        if self.__wings > 0:
            print(f"This animal has {self.__wings} wings")
        self.move()
        self.eat()
        self.birth()
        try:
            self.hibernate()
        except:
            pass
        print()


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.__coldBlooded = False
        self.__skinType = "fur"

    def birth(self):
        print("This animal gives birth to live young")


class Reptile(Animal):
    def __init__(self):
        super().__init__()
        self.__coldBlooded = True
        self.__skinType = "scales"

    def birth(self):
        print("This animal lays eggs")

    def hibernate(self):
        print("This animal hibernates")

    def getInfo(self):
        super().getInfo()


class Tortoise(Reptile):
    def __init__(self):
        super().__init__()
        self.__tail = True
        self.__legs = 4

    def move(self):
        print("This animal walks")

    def eat(self):
        print("This animal is a herbivore")

    def getInfo(self):
        print("Tortoise:")
        super().getInfo()


class Turtle(Reptile):
    def __init__(self):
        super().__init__()
        self.__tail = True
        self.__legs = 4

    def move(self):
        print("This animal crawls and swims")

    def eat(self):
        print("This animal is an omnivore")

    def getInfo(self):
        print("Turtle:")
        super().getInfo()


class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.__tail = True
        self.__legs = 0

    def move(self):
        print("This animal slithers")

    def eat(self):
        print("This animal is a carnivore")

    def getInfo(self):
        print("Snake:")
        super().getInfo()


class Otter(Mammal):
    def __init__(self):
        super().__init__()
        self.__tail = True
        self.__legs = 4

    def move(self):
        print("This animal walks and swims")

    def eat(self):
        print("This animal is an omnivore")

    def getInfo(self):
        print("Otter:")
        super().getInfo()


class Gorilla(Mammal):
    def __init__(self):
        super().__init__()
        self.__tail = False
        self.__legs = 2
        self.__arms = 2

    def move(self):
        print("This animal walks and climbs")

    def eat(self):
        print("This animal is a herbivore")

    def getInfo(self):
        print("Gorilla:")
        super().getInfo()
        print("")


class Bat(Mammal):
    def __init__(self):
        super().__init__()
        self.__tail = True
        self.__legs = 2
        self.__wings = 2

    def move(self):
        print("This animal flies")

    def eat(self):
        print("This animal is an omnivore")

    def hibernate(self):
        print("This animal hibernates")

    def getInfo(self):
        print("Bat:")
        super().getInfo()


def main():
    tortoise = Tortoise()
    turtle = Turtle()
    snake = Snake()
    otter = Otter()
    gorilla = Gorilla()
    bat = Bat()

    tortoise.getInfo()
    turtle.getInfo()
    snake.getInfo()
    otter.getInfo()
    gorilla.getInfo()
    bat.getInfo()


if __name__ == "__main__":
    main()
