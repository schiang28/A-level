CONSTANT_PI = 3.14159


def circle_area(radius_in):
    radius_out = CONSTANT_PI * radius_in ** 2
    return radius_out


r = float(input("enter radius"))
print(circle_area(r))

# repl.it link --> https://replit.com/join/khxcojnybb-schiang28