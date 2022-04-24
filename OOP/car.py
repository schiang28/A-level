#############################
# Class Definitions
#############################


class Models:
    Bmw = "BMW"
    Audi = "Audi"
    Harley = "Harley Davidson"
    Suzuki = "Suzuki"


class Colours:
    Red = "Red"
    Yellow = "Yellow"


# Implement the classes given in the class diagram.


class Motor:
    def __init__(self, power, weight):
        self.__power = power
        self.__weight = weight

    @property
    def power(self):
        return self.__power

    @property
    def weight(self):
        return self.__weight


class Vehicle:
    def __init__(self, numwheels):
        self.__colour = ""
        self.__numwheels = numwheels

    @property
    def colour(self):
        return self.__colour

    @property
    def numwheels(self):
        return self.__numwheels

    @colour.setter
    def colour(self, c):
        self.__colour = c


class Car(Vehicle):
    def __init__(self, model, numwheels=4):
        self.__model = model
        self.__motor = None
        super().__init__(numwheels)

    @property
    def model(self):
        return self.__model

    @property
    def motor(self):
        raise NotImplementedError()

    @motor.setter
    def motor(self, m):
        self.__motor = m

    def get_power(self):
        return self.__motor.power

    def paint(self, s):
        self.colour = s


class Motorbike(Vehicle):
    def __init__(self, model, numwheels=2):
        self.colour = "Black"
        self.__model = model
        self.__motor = None
        super().__init__(numwheels)

    @property
    def model(self):
        return self.__model

    @property
    def motor(self):
        raise NotImplementedError()

    @property
    def power(self):
        self.get_power()

    @motor.setter
    def motor(self, m):
        self.__motor = m

    def get_power(self):
        return self.__motor.power


# Read the code below. There is one line indicated which needs finishing (There may be other typos!)
class Garage:
    def __init__(self):
        self.__vehicles = []

    def add_vehicle(self, v):
        self.__vehicles.append(v)

    def __len__(self):
        return len(self.__vehicles)

    def __getitem__(self, vnum):
        if 0 <= vnum < len(self):
            # Return vehicle give by vnum
            return self.__vehicles[vnum]
        else:
            raise IndexError


#############################
# Main Program
#############################
bmw = Car(Models.Bmw)
bmw.motor = Motor(power=1000, weight=123)
bmw.paint(Colours.Yellow)

audi = Car(Models.Audi)
audi.motor = Motor(power=1500, weight=97.5)
audi.paint(Colours.Red)

harley = Motorbike(Models.Harley)
harley.motor = Motor(power=500, weight=50)

g = Garage()
for v in (bmw, audi, harley):
    g.add_vehicle(v)

try:
    print(harley.motor)
    print("Error! Should not be able to do this 1")
except NotImplementedError:
    pass

try:
    harley.power = 3000
    print("Error! Should not be able to do this 2")
except AttributeError:
    pass

try:
    harley.model = Models.Suzuki
    print("Error! Should not be able to do this 3")
except AttributeError:
    pass

try:
    bmw.numwheels = 3
    print("Error! Should not be able to do this ")
except AttributeError:
    pass


print("Vehicles in the garage:")
for i, v in enumerate(g):
    print(
        f"Vehicle {i} is a {v.colour} {v.model} with a {v.get_power()} horsepower engine and {v.numwheels} wheels"
    )
