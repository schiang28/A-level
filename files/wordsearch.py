# change 3 and 4th letters to be ##
with open("board.bin", "rb+") as f:
    f.seek(2)
    f.write(bytearray([ord("#"), ord("#")]))

with open("board.bin", "rb") as f:
    data = list(f.read())
    print(data)
    data = [chr(n) for n in data]

print(data)
