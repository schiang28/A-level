while True:
    print("Console Menu Application")
    choice = input("s to search, a to add, e to edit, d to delete, q to quit")

    if choice == "q":
        break

    elif choice == "s":
        with open("recordinfo.csv") as file:
            f = [i.split(",") for i in file.read().splitlines()]
        c1 = input(("enter 0,1,2 to search by ID, firstname or surname"))
        c2 = input("enter what your searching for")
        found = [i for i in f if i[int(c1)] == c2]
        if found:
            print(found)
        else:
            print("no record found with this id")

    elif choice == "a":
        a1 = input("enter ID")
        a2 = input("enter firstname")
        a3 = input("enter lastname")
        a4 = input("enter dob")
        a5 = input("enter class")
        with open("recordinfo.csv", "a") as file:
            file.write("\n")
            file.write(",".join([a1, a2, a3, a4, a5]))
        print(f"{[a1,a2,a3,a4,a5]} written to file")

    elif choice == "d":
        c1 = input("enter ID of record to remove")
        with open("recordinfo.csv") as file:
            f = [i.split(",") for i in file.read().splitlines()]
        found = [i for i in f if i[0] != c1]
        if len(found) < len(f):
            with open("recordinfo.csv", "w") as file:
                for element in found:
                    file.write(",".join(element) + "\n")
        else:
            print("record with id not found")

    elif choice == "e":
        c1 = input("enter ID of record to edit")
        with open("recordinfo.csv") as file:
            f = [i.split(",") for i in file.read().splitlines()]
        found = False
        for i in f:
            if i[0] == c1:
                found = True
                i[0] = input("enter new id")
                i[1] = input("enter new first name")
                i[2] = input("enter new last name")
                i[3] = input("enter new dob")
                i[4] = input("enter new class")
                with open("recordinfo.csv", "w") as file:
                    for element in f:
                        file.write(",".join(element) + "\n")
                break
        if not found:
            print("record with entered id not found")
    else:
        print("not valid input")
