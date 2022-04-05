string = input("Enter a string:")


def palindrome():
    if string == string[::-1]:
        print("The string is a palindrome")
    else:
        print("Not a palindrome")


def test():
    input("Enter a string:")
    palindrome()
