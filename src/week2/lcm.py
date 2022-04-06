# lcm - least common multiple
def lcm(x, y):
    if x > y:
        x, y = y, x
    for x in range(x, 0, -1):
        if x % x == 0 and y % x == 0:
            return x


num1 = 25
num2 = 50

print(str(lcm(num1, num2)))
# print("The L.C.M. is", compute_lcm(num1, num2))
