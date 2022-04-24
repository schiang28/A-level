def is_odd(number_in):
    if int(number_in) % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


while True:
    num = input("enter number, STOP to end")
    if num == "STOP":
        break
    is_odd(num)