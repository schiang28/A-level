def lower_num(num1, num2):
    if num1 <= num2:
        return num1
    else:
        return num2


first = int(input("Enter the first num: "))
second = int(input("Enter second num: "))

lowest = lower_num(first, second)
print("lowest number", lowest)