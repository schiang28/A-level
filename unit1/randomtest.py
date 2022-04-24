f = open("birdFile.txt", "w")
numRecs = int(input("How many records do you wish to write?"))
for index in range(numRecs):
    birdName = input("Enter bird name: ")
    birdsReported = input("Enter number of birds reported: ")

    f.write(f"{birdName}, {birdsReported} \n")

f.close()
