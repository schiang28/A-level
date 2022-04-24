"""ls = []
while True:
    x = input("")
    if x == "Stop":
        break
    ls.append(x)

first = ls[0]
total = 0
count = 0
for i in ls:
    if int(i) != int(first):
        total += int(i)
        count += 1

print(total)
print(round(total / float(count), 2))
"""

ls = []
while True:
    x = input("")
    if x == "Stop":
        break
    ls.append(x)

total = 0
count = 0
for i in ls:
    if ls[0] not in i:
        total += int(i)
        count += 1

print(total)
print(round(total / float(count), 3))