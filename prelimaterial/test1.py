Index = 0
self.__ListPositionOfTile = 0
GridString = self.__CreateTopLine()
GridLine,Index = self.__CreateEvenLineIndices(Index,True)
GridString += GridLine
self.__ListPositionOfTile += 1
GridLine,Index = self.__CreateOddLineIndices(Index)
GridString += GridLine
for count in range (1, self._Size - 1, 2):
self.__ListPositionOfTile += 1
GridLine,Index = self.__CreateEvenLineIndices(Index,False)
GridString += GridLine
self.__ListPositionOfTile += 1
GridLine,Index = self.__CreateOddLineIndices(Index)
GridString += GridLine
return GridString + self.__CreateBottomLine()
