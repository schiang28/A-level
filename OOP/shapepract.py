from math import pi


class Colour:
    Black = "Black"
    Blue = "Blue"
    Red = "Red"


# Write your code in here ...


class Shape:
    def __init__(self, shapeid):  # , colour, position):
        self.__shapeid = shapeid
        self.__colour = Colour.Black
        self.__position = (0, 0)

    @property
    def shapeid(self):
        return self.__shapeid

    @property
    def colour(self):
        return self.__colour

    @property
    def position(self):
        return self.__position

    @colour.setter
    def colour(self, value):
        if value in [Colour.Black, Colour.Blue, Colour.Red]:
            self.__colour = value
        else:
            raise ValueError

    @position.setter
    def position(self, value):
        self.__position = value

    def perimeter(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

    def resize(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, shapeid):
        super().__init__(shapeid)
        # self.__shapeid = shapeid
        self.__length = 1
        self.__width = 2

    @property
    def shapeid(self):
        return self.__shapeid

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    def perimeter(self):
        return self.length * 2 + self.width * 2

    def area(self):
        return self.length * self.width

    def resize(self, length, width):
        self.__length = length
        self.__width = width

    def __repr__(self):
        return f"{self.colour} rectangle at {self.position} of dimensions {self.length} x {self.width}"


class Circle(Shape):
    def __init__(self, shapeid):
        super().__init__(shapeid)
        # self.__shapeid = shapeid
        self.__radius = 1

    @property
    def radius(self):
        return self.__radius

    def perimeter(self):
        return self.radius * 2 * pi

    def area(self):
        return self.radius ** 2 * pi

    def resize(self, value):
        self.__radius = value

    def __repr__(self):
        return f"{self.colour} Cicle at {self.position} with radius {self.radius}"


class Square(Rectangle):
    def __init__(self, shapeid):
        super().__init__(shapeid)
        # self.__shapeid = shapeid
        self.__side = 1

    @property
    def side(self):
        return self.__side

    def resize(self, value):
        self.__side = value

    def __repr__(self):
        return f"{self.colour} square at {self.position} with side {self.side}"


class Canvas:
    Square = "Square"
    Circle = "Circle"
    Rectangle = "Rectangle"

    def __init__(self):
        self.__nextid = 0
        self.__shapes = {}

    def add_shape(self, name):
        self.__nextid += 1
        # print(self.__shapes)
        if name == "Square":
            instance = Square(self.__nextid)
            self.__shapes[self.__nextid] = instance
            return self.__nextid
        elif name == "Circle":
            instance = Circle(self.__nextid)
            self.__shapes[self.__nextid] = instance
            return self.__nextid
        elif name == "Rectangle":
            instance = Rectangle(self.__nextid)
            self.__shapes[self.__nextid] = instance
            return self.__nextid
        else:
            raise ValueError

    def get_shape(self, shapeid):
        if shapeid in self.__shapes.keys():
            return self.__shapes[shapeid]
        else:
            raise IndexError

    def get_area(self):
        total = 0
        for i in self.__shapes.values():
            total += i.area()
        return total

    def __repr__(self):
        s = "\n".join(str(s) for s in self.__shapes.values())
        return s


# Do not change below here ...

c = Canvas()
while True:
    print(
        """
Menu
1) Add shape
2) Recolour shape
3) Resize shape
4) Move shape
5) Print canvas
6) Exit"""
    )
    option = int(input())
    if option == 1:
        print(
            """
Menu
1) Circle
2) Rectangle
3) Square"""
        )
        option = int(input())
        if option == 1:
            sid = c.add_shape(Canvas.Circle)
        elif option == 2:
            sid = c.add_shape(Canvas.Rectangle)
        elif option == 3:
            sid = c.add_shape(Canvas.Square)
        else:
            sid = None

        if sid is not None:
            print(f"Added shape with ID {sid}")
    elif option == 2:
        sid = int(input("Enter shape ID for recolouring "))
        try:
            s = c.get_shape(sid)
            col = input("Enter new colour: ")
            s.colour = col
        except IndexError:
            print("Canvas does not have that shape")
    elif option == 3:
        sid = int(input("Enter shape ID for resizing "))
        try:
            s = c.get_shape(sid)
            dim = [
                int(i)
                for i in input("Enter new dimensions separated by spaces: ").split()
            ]
            s.resize(*dim)
        except IndexError:
            print("Canvas does not have that shape")
    elif option == 4:
        sid = int(input("Enter shape ID for moving "))
        try:
            s = c.get_shape(sid)
            pos = tuple(
                [
                    int(i)
                    for i in input("Enter new position separated by spaces: ").split()
                ]
            )
            s.position = pos
        except IndexError:
            print("Canvas does not have that shape")
    elif option == 5:
        print(c)
        print(c.get_area())
    elif option == 6:
        break
