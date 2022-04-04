from typing import Any

def fibonacci(n):
    try:
        n = int(n)
        if n >= 0:
            if n==0:
                return 0
            elif n==1 or n==2:
                return 1
            else:
                return fibonacci(n-1) + fibonacci(n-2)
        else:
            return "Input must be non-negative"
    except ValueError:
        return "Wrong type of input."

    n=int(input("Enter the value of n: "))
    print(fibonacci(n))

if __name__ == "__main__":
    fibonacci()