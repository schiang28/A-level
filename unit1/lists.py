from collections import Counter


def three():
    ls = []
    for _ in range(10):
        ls.append(ord(input("")))

    print(ls)


def four():
    letter_count = {}
    for char in "abcdefghijklmnopqrstuvwxyuz":
        letter_count[char] = 0

    s = input()
    for c in s:
        if c.isalpha():
            letter_count[c.lower()] += 1

    for k, v in letter_count.items():
        print(k, v)


def four2():
    for k, v in Counter(input().lower()).items():
        if k.isalpha():
            print(k, v)


four2()