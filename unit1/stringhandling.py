# w = input()
# print(len(w.split(" ")))

"""x = input("")
y = input("")

if x in y:
    print("y")
else:
    print("n")
"""

"""
x, y = input(""), input("")

for char in range(len(y) + 1, 0, -1):
    if y[:char] in x:
        print(y[:char])
        break
"""

# w = input()
# print(w[::-1])

"""
x, y = input(), input()
if sorted(x) == sorted(y):
    print("is anagram")
else:
    print("nope")
"""
"""
w = input()
if w == w[::-1]:
    print("y")
else:
    print("n")
"""

"""
i, j = input(), input()
print(j[: max([x for x in range(min([len(i), len(j)])) if i[-x:] == j[:x]])])
"""
