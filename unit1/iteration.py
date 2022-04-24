n1 = int(input("enter num 1 "))
n2 = int(input("enter num 2 "))
t1, t2 = n1, n2
while t1 != t2:
    if t1 > t2:
        t1 = t1 - t2
    else:
        t2 = t2 - t1
result = t1
print(f"{result} is GCF of {n1} and {n2}")