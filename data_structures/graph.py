class NoEdge(Exception):
    pass


#############################
# Abstract Base Class
#############################
class Graph:

    ADJACENT = 1
    NOT_ADJACENT = None

    def __init__(self, numv):
        self.__numv = numv

    @property
    def numv(self):
        return self.__numv

    def setAdjacent(self, fr, to, weight=None):
        raise NotImplementedError

    def delAdjacent(self, fr, to):
        raise NotImplementedError

    def allAdjacent(self, v):
        raise NotImplementedError

    def isAdjacent(self, fr, to):
        raise NotImplementedError

    def getWeight(self, fr, to):
        raise NotImplementedError


##################################
# Undirected Graph
# Unweighted Graph
# Implemented using an Adjacency Matrix
##################################
class UndirectedUnweightedMatrix(Graph):
    def __init__(self, numv):
        super().__init__(numv)
        self._data = [[Graph.NOT_ADJACENT for _ in range(numv)] for _ in range(numv)]

    def setAdjacent(self, fr, to):
        self._data[fr][to] = Graph.ADJACENT
        self._data[to][fr] = Graph.ADJACENT

    def delAdjacent(self, fr, to):
        self._data[fr][to] = Graph.NOT_ADJACENT
        self._data[to][fr] = Graph.NOT_ADJACENT

    def allAdjacent(self, v):
        return [
            to
            for to, connection in enumerate(self._data[v])
            if connection != Graph.NOT_ADJACENT
        ]

    def isAdjacent(self, fr, to):
        return self._data[fr][to] != Graph.NOT_ADJACENT


##################################
# Undirected Graph
# Unweighted Graph
# Implemented using an Adjacency List
##################################
class UndirectedUnweightedList(Graph):
    def __init__(self, numv):
        super().__init__(numv)
        self._data = [[] for _ in range(numv)]

    def setAdjacent(self, fr, to):
        if to not in self._data[fr]:
            self._data[fr].append(to)
            self._data[to].append(fr)

    def delAdjacent(self, fr, to):
        if to in self._data[fr]:
            self._data[fr].remove(to)
            self._data[to].remove(fr)

    def allAdjacent(self, v):
        return self._data[v]

    def isAdjacent(self, fr, to):
        return to in self._data[fr]


##################################
# Directed Graph
# Unweighted Graph
# Implemented using an Adjacency List
##################################
class DirectedUnweightedList(UndirectedUnweightedList):
    def setAdjacent(self, fr, to):
        if to not in self._data[fr]:
            self._data[fr].append(to)

    def delAdjacent(self, fr, to):
        if to in self._data[fr]:
            self._data[fr].remove(to)


##################################
# Directed Graph
# Unweighted Graph
# Implemented using an Adjacency Matrix
##################################

class DirectedUnweightedMatrix(UndirectedUnweightedMatrix):
    def setAdjacent(self, fr, to):
        self._data[fr][to] = Graph.ADJACENT

    def delAdjacent(self, fr, to):
        self._data[fr][to] = Graph.NOT_ADJACENT


##################################
# Undirected Graph
# Weighted Graph
# Implemented using an Adjacency Matrix
##################################

class UndirectedWeightedMatrix(UndirectedUnweightedMatrix):
    def setAdjacent(self, fr, to, weight):
        self._data[fr][to] = weight
        self._data[to][fr] = weight

    def getWeight(self, fr,to):
        if self._data[fr][to] == Graph.NOT_ADJACENT:
            raise NoEdge(f"{fr} and {to} are not adjacent")
        return self._data[fr][to]

##################################
# Undirected Graph
# Weighted Graph
# Implemented using an Adjacency List
##################################
class UndirectedWeightedList(Graph):
    def __init__(self, numv):
        super().__init__(numv)

    def setAdjacent(fr, to, weight):
        pass

    def delAdjacent(fr, to):
        pass

    def allAdjacent(v):
        pass

    def isAdjacent(fr, to):
        pass

    def getWeight(fr, to):
        pass


##################################
# Directed Graph
# Weighted Graph
# Implemented using an Adjacency List
##################################
class DirectedWeightedList(Graph):
    def __init__(self, numv):
        super().__init__(numv)

    def setAdjacent(fr, to, weight):
        pass

    def delAdjacent(fr, to):
        pass

    def allAdjacent(v):
        pass

    def isAdjacent(fr, to):
        pass

    def getWeight(fr, to):
        pass


##################################
# Directed Graph
# Weighted Graph
# Implemented using an Adjacency Matrix
##################################
class DirectedWeightedMatrix(Graph):
    def __init__(self, numv):
        super().__init__(numv)

    def setAdjacent(fr, to, weight):
        pass

    def delAdjacent(fr, to):
        pass

    def allAdjacent(v):
        pass

    def isAdjacent(fr, to):
        pass

    def getWeight(fr, to):
        pass
