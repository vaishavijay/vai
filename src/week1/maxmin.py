from random import randint
try:
    while True:
        x=input("MAXIMUM:")
        y=input("MINIMUM:")
        answer = int(randint(x, y))
        while True:
            z=int(input("guess"))
            if (z==answer):
                print("correct!")
            else:
                print("you failed lol")
        a=input("playagain")
        if (a=="y"):
            break
except:
    print("error")