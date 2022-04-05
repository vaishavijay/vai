class Fact:
    def factorial(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f


print("Enter a Number: ", end="")
num = int(input())

ob = Fact()
print("\nFactorial of", num, "=", ob.factorial(num))

#help - https://codescracker.com/python/program/python-program-find-factorial-of-number.htm

if __name__ == "__main__":
    Fact()