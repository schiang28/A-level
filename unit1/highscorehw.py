try:
    with open("scores.txt") as file:
        f = file.read().splitlines()
    if len(f) != 3:
        raise ValueError("wrong number of scores")
    print("max score is", max([int(i) for i in f]))
except FileNotFoundError:
    print("file not found")
except ValueError:
    print("score not positive integer")
except IOError:
    print("file is locked")
