from attr import field

print("test")

f = open("birdFile.txt", "r")
birdNameSearch = input("What bird are you searching for?")
for index in range(8):
    try:
        field = f.readline().strip().split(", ")  # investigate .strip() .split()?
        birdname, birdsseen = field[0], field[1]
        if birdname == birdNameSearch:
            print(birdname, birdsseen)
            break
    except:
        print("none")
        break


f.close()
