def harshad(n):
    total = 0
    for i in str(n):
        total += int(i)
    if n % total == 0:
        return True
    return False


count = 1
num = int(input())
n = 1
while True:
    if harshad(n):
        if count == num:
            break
        count += 1
    n += 1

print(n)
