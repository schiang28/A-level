from collections import namedtuple
from datetime import datetime

Employee = namedtuple("Employee", "EmployeeCode Surname Firstname DateOfBirth")

Employees = []

Employees.append(
    Employee
    (
        EmployeeCode = "SMI001", 
        Surname = "SMITH", 
        Firstname = "JOHN", 
        DateOfBirth =  datetime(1996,12,5)
    ))

Employees.append(
    Employee
    (
        EmployeeCode = "BLO003", 
        Surname = "BLOGGS", 
        Firstname = "JANE", 
        DateOfBirth =  datetime(1997,7,31)
    ))

Employees.append(
    Employee
    (
        EmployeeCode = "ACE223", 
        Surname = "ACE", 
        Firstname = "JACK", 
        DateOfBirth =  datetime(2002,5,11)
    ))

Employees.append(
    Employee
    (
        EmployeeCode = "BLA055", 
        Surname = "BLACK", 
        Firstname = "JILL", 
        DateOfBirth =  datetime(1997,7,31)
    ))

Employees.append(
    Employee
    (
        EmployeeCode = "CHI135", 
        Surname = "CHIANG", 
        Firstname = "SOPHIE", 
        DateOfBirth =  datetime(2005,7,28)
    ))

for i in Employees:
    print(i)


class HashTable:
    def __init__(self, size):
        self.hashstore = [None] * size
        self.size = size

    def add(self, key, value):
        # SMI001 -> N where we store 0 at the calculated position
        # apply ascii hash to the key (mod self.size)
        # and store the value at that location

        if None in self.hashstore: # there is still free space
            position = 0
            for char in key:
                position += ord(char)
            position = position % self.size

            # deal with collisions
            while True:
                if self.hashstore[position] == None:
                    self.hashstore[position] = value
                    print("Hashed successfully!")
                    break
                else:
                    position = (position + 1) % self.size

    def get(self, key):
        position = 0
        for char in key:
            position += ord(char)
        position = position % self.size

        originalPosition = position
        while True:
            # found blank, doesn't exist
            if self.hashstore[position] == None:
                return None

            # check if found employee that hashes the same
            index = self.hashstore[position]
            employeeIDAtIndex = Employees[index]

            if employeeIDAtIndex.EmployeeCode == key:
                return employeeIDAtIndex
            
            # gone through whole hash table, and not found
            if position == originalPosition - 1:
                return None

            position = (position + 1) % self.size

hashTable = HashTable(100)
for i in range(len(Employees)):
    code = Employees[i][0]
    loc = i
    hashTable.add(code, i)

# MENU
print("WELCOME TO MY EMPLOYEE CODE LOOKUP DATABASE SERVICE!")

while True:
    code = input("enter code to search:")
    print(hashTable.get(code))