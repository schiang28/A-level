class BuildKind:
    Bungalow = "Bungalow"
    Detached = "Detached"
    Flat = "Flat"


class Building:
    def __init__(self, kind, rooms, floors):
        self.__kind = kind
        self.__rooms = rooms
        self.__floors = floors
        self.__owner = ""

    @property
    def kind(self):
        return self.__kind

    @property
    def rooms(self):
        return self.__rooms

    @property
    def floors(self):
        return self.__floors

    # Create a getter and setter for the owner property

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, name):
        self.__owner = name

    def __repr__(self):
        return f"{self.owner}'s {self.kind} with {self.rooms} rooms over {self.floors} floor{'s' if self.floors > 1 else ''}."


class Bungalow(Building):
    def __init__(self, rooms):
        super().__init__(kind=BuildKind.Bungalow, rooms=rooms, floors=1)


class Detached(Building):
    def __init__(self, rooms):
        super().__init__(kind=BuildKind.Detached, rooms=rooms, floors=2)


class Flat(Building):
    def __init__(self, rooms, floors):
        super().__init__(kind=BuildKind.Flat, rooms=rooms, floors=floors)


class Street:
    def __init__(self, name):
        self.__buildings = []
        self.__name = name

    @property
    def name(self):
        return self.__name

    def add_building(self, b):
        self.__buildings.append(b)

    def __len__(self):
        return len(self.__buildings)

    def __getitem__(self, i):
        return self.__buildings[i]

    def __repr__(self):
        result = f"Street: {self.name}, Buildings: {len(self)}\n"
        for b in self.__buildings:
            result += "    " + str(b) + "\n"
        return result


class City:
    def __init__(self, name):
        self.__streets = []
        self.__name = name

    @property
    def name(self):
        return self.__name

    def add_street(self, street):
        self.__streets.append(street)

    def __len__(self):
        return len(self.__streets)

    def __getitem__(self, i):
        return self.__streets[i]

    def __repr__(self):
        result = f"City: {self.name}, Streets: {len(self)}\n"
        for s in self.__streets:
            result += "  " + str(s) + "\n"
        return result


s1 = Street("High St")
b1 = Bungalow(rooms=5)
b1.owner = "John"

b2 = Detached(rooms=8)
b2.owner = "Jamal"

s1.add_building(b1)
s1.add_building(b2)


s2 = Street("Station Rd")
b3 = Flat(rooms=20, floors=4)
b3.owner = "Sasha"

b4 = Detached(rooms=6)
b4.owner = "Rhea"

s2.add_building(b3)
s2.add_building(b4)

city = City("Newport")
city.add_street(s1)
city.add_street(s2)

print(city)

for snum in range(len(city)):
    street = city[snum]
    for bnum in range(len(street)):
        building = street[bnum]
        print(building)
