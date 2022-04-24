with open("Blank.bmp", "rb") as fb:
    # returns bytearray object
    data = fb.read()

# print(data)
iArr = list(data)
# print(iArr)

iArr[175] = 255
iArr[176] = 255

iArr[225] = 128
iArr[227] = 128

iArr[171] = 128
iArr[173] = 128

with open("Blank2.bmp", "wb") as fb:
    fb.write(bytearray(iArr))
