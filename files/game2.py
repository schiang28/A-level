with open("board.bin", "rb") as f:
    data = list(f.read())

print(data)

# print grid
row = ""
for i in range(len(data)):
    if len(row) == 8:
        print(row)
        row = ""
    else:
        row += chr(data[i])

# get coords
start = [int(xy) for xy in input("x,y:").split(",")]
end = [int(xy) for xy in input("x,y:").split(",")]
word = input("Word seen?:")
