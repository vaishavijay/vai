def swap(age1, age2):
    if age1 > age2:
        yuh = age1
        age1 = age2
        age2 = yuh
    return age1, age2


def test():
    x = int(input("Number 1 "))
    y = int(input("Number 2"))
    swap(x, y)


if __name__ == "__main__":
    test()
