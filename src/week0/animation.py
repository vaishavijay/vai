def tree():
    n = int(input("How tall would you like your pyramid to be?: "))
    p = n - 1
    for i in range(0, n):
        for x in range(0, p):
            print(end=" ")
        p = p - 1
        for x in range(0, i+1):
            print("❒ ", end="")
        print(" ")

if __name__ == "__main__":
    tree()