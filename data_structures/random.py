from graph import *

#g = UndirectedWeightedList(7)
g = UndirectedWeightedMatrix(7)
g.setAdjacent(1,2,weight=2)
g.setAdjacent(1,4,weight=5)
g.setAdjacent(3,2,weight=14)
g.setAdjacent(3,5,weight=34)
g.setAdjacent(2,5,weight=4)
g.setAdjacent(2,4,weight=5)
g.setAdjacent(5,4,weight=58)

print(g.allAdjacent(2))

g.delAdjacent(2,5)
print(g.allAdjacent(2))
print(g.getWeight(4,5))

try:
    print(g.getWeight(1,5))
except NoEdge as e:
    print("Error: ",e)

if g.isAdjacent(2,3):
    print("2 and 3 are adjacent")

if not g.isAdjacent(3,4):
    print("4 and 3 are not adjacent")