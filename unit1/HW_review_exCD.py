def ToDecimal(hexdigit):
    nls = [str(i) for i in range(10)]
    if hexdigit == "A":
        value = 10
    elif hexdigit == "B":
        value = 11
    elif hexdigit == "C":
        value = 12
    elif hexdigit == "D":
        value = 13
    elif hexdigit == "E":
        value = 14
    elif hexdigit == "F":
        value = 15
    elif hexdigit in nls:
        value = ord(hexdigit) - 48
    else:
        value = -1
    return value


for count in range(1, 3):
    hexstring = input()
    number = 0
    for hexdigit in hexstring:
        value = ToDecimal(hexdigit)
        number = number * 16 + value
    print(number)
