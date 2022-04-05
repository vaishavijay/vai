# lcm - least common multiple
def lcm(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1

    for x in range(num1, 0, -1):
        if num1 % x == 0 and num2 % x == 0:
            return x


num1 = 30
num2 = 50

print(str(lcm(num1, num2)))
# print("The L.C.M. is", compute_lcm(num1, num2))

if __name__ == "__main__":
    lcm()
