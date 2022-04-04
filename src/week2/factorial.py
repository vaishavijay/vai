from math import factorial


class Factorial:

    def factorial(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f


n = int(input("What number would you like to find the factorial of?:"))

obj = Factorial()
f = obj.fact(n)
print("The factorial is:", f)

if __name__ == "__main__":
    factorial()