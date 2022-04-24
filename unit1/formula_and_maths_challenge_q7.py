start = int(input("enter starting day of month"))
numdays = int(input("enter number of days"))
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
print("\t".join(days))


def method_1():
    cal = "   \t" * (start - 1)
    count = start
    for i in range(1, numdays + 1):
        cal += str(i) + " " * (3 - (len(str(i)))) + "\t"
        if count % 7 == 0:
            cal += "\n"
        count += 1
    print(cal)


def method_2():
    daynum = list(map(str, range(1, numdays + 1)))
    cal = ["", "", "", "", "", "", ""]

    count = 0
    for i in range(start - 1, 7):
        cal[i] = daynum[count]
        count += 1

    print("\t".join(cal))

    if numdays - (count + 1) % 7 == 0:
        week = (numdays - (count + 1)) // 7
    else:
        week = (numdays - (count + 1)) // 7 + 1

    for _ in range(week):
        for i in range(7):
            if count >= numdays:
                cal[i] = " "
            else:
                cal[i] = daynum[count]
            count += 1
        print("\t".join(cal))