{% include navigation.html %}

# TT2: Python Classes

**Hack 1: Organize files, directories and menus for the first 3 weeks.**
import src.week0.animation
import src.week0.cafemenu
import src.week0.matrix
import src.week0.swap
import src.week1.fibonacci
import src.week1.infodb
import src.week2.lcm

main_menu = []
math_menu = [
    ["Number Swap", src.week0.swap.swap],
    ["Matrix", src.week0.matrix.matrix],
    ["Fibonacci", src.week1.fibonacci.fibonacci],
    ["LCM Calculator", src.week2.lcm.lcm]
]

patterns_menu = [
    ["Cafe Menu", src.week0.cafemenu.print_menu1],
    ["Pyramid Animation", src.week0.animation.pyramid],
    ["InfoDB Lists/Loops", src.week1.infodb.driver],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", math_menu])
    menu_list.append(["Patterns", patterns_menu])
    buildMenu(title, menu_list)


def math_menu():
    title = "Math Submenu" + banner
    buildMenu(title, math_menu)


def patterns_menu():
    title = "Patterns Submenu" + banner
    buildMenu(title, patterns_menu)


def buildMenu(banner, options):
    # header for menu
    global action
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try
    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()


**Hack 2: Factorial function using classes, providing implementation of cal**
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

Hack 3: Math function (LCM)
    def lcm(x, y):
        if x > y:
            x, y = y, x
        for x in range(x, 0, -1):
            if x % x == 0 and y % x == 0:
                return x


    num1 = 30
    num2 = 50

    print(str(lcm(num1, num2)))
    # print("The L.C.M. is", compute_lcm(num1, num2))


# TT1: Data Structures 

### Notes: 

The digital divide is the name of the divide between differing access to the internet across socioeconomic, geographic, or demographic regions, such as between developing and first world countries. Some places have limited access to computers and websites. The internet may be used to protect and advocate for the government in these places. This divide affects both individuals and groups, and raises equity issues. 

Computing biases are biases written into computer code that can reflect the biases of the programmer. These biases can be embedded into any layer of software development. Programmers should take action to avoid introducing these biases whenever possible. This can include gearing towards a particular audience, or Netflix biasing towards showing their own shows.

Crowdsourcing is the process of enlisting the service of the crowd, large numbers of people, with or without notifying them. This could be things such as getting data from large amounts of people, or citizen science projects where many many people collaborate. 
Computers can raise legal or ethical concerns regarding copyright. User data must be stored securely.

Data Structures Project: https://replit.com/@vaishavijay/Cafe-Menu
* Café Menu: (allows user to choose between drinks and pastries)
* Boat Animation: https://replit.com/@vaishavijay/vaishavijay#main.py

### Code Snippets + Learnings: 

    print("Welcome to the Café! What would you like to order?")
        def print_menu1():
            print('Hot Coffee' )
            print('Iced Coffee' )
            print('Pastries' )
            print('Exit ' )
            runOptions()

The above code prints out options for the user.

    def hot():
        print('You chose \'Hot Coffee\'')
    def cold():
        print('You chose \'Iced Coffee\'')
    def past():
        print('You chose \'Pastries\'')

The above code defines variables and shows what the program will respond to the user with after they make their selection.

    while True:
        try:
            option = int(input('Please enter your choice 1-4: '))
            if option == 1:
                hot()
            elif option == 2:
                cold()
            elif option == 3:
                past()
            # Exit menu    
            elif option == 4:  
                print('Thank you for visiting our café! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

The above code displays the choice menu. The selection of the number 1-4 that the user makes determines what variable the program proceeds to, to which selected text will be displayed (as seen above).

        if __name__=='__main__':
           # print_menu1()
            print_menu2()

The defined code allows code/menu to run overall.

# Challenges (InfoDB Code): 

    
    # Hack 1: InfoDB lists

    InfoDb = []
    # List with dictionary records placed in a list
    InfoDb.append({
        "FirstName": "Vaishavi",
        "LastName": "Jayashankar",
        "DOB": "March 15",
        "COB": "San Diego",
        "Email": "vaishavi2005@gmail.com",
        "T3Classes":["AP Calc","APEL","AP Bio","Chamber Orchestra", "APCSP"]
    })

    InfoDb.append({
        "FirstName": "Shreya",
        "LastName": "Sapkal",
        "DOB": "December 12",
        "COB": "Detroit",
        "Email": "shreyas959@gmail.com",
        "T3Classes":["AP Calc","AP Physics","Raquet Sports","Honors POE","APEL"]
    })

    # given an index this will print InfoDb content
    def print_data(n):
        print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
        print("\t", "T3Classes: ", end="")  # \t is a tab indent, end="" make sure no return occurs
        print(", ".join(InfoDb[n]["T3Classes"]))  # join allows printing a string list with separator
        print()

    # Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
    def for_loop():
        for n in range(len(InfoDb)):
            print_data(n)

    ## hack 2a: def for_loop()
    # for loop iterates on length of InfoDb
    # def for_loop():
    #     for n in range(len(InfoDb)):
    #         print_data(n)

    ## hack 2b: def while_loop(0)
    # while loop contains an initial n and an index incrementing statement (n += 1)
    def while_loop():
        n = 0
        while n < len(InfoDb):
            print_data(n)
            n += 1
        return

    ## hack 2c : def recursive_loop(0)
    # recursion simulates loop incrementing on each call (n + 1) until exit condition is met
    def recursive_loop0(): # Pass an argument and sometimes do not pass an argument, so I just remove all the arguments - Gigi Guan
        #Those that already have a function, then I made a new one without it and call if recursively - Gigi Guan
        n = 0
        recursive_loop1(n)
        return

    def recursive_loop1(n):
        if n < len(InfoDb):
            print_data(n)
            recursive_loop1(n + 1)
        return # exit condition


    def driver():
        print("For loop")
        for_loop()
        print("While loop")
        while_loop()  # requires initial index to start while
        print("Recursive loop")
        recursive_loop0()  # requires initial index to start recursion


    if __name__ == "__main__":
        driver()
        
# Challenges (Fibonacci Code): 

    from typing import Any


    def fibonacci(n):
        try:
            n = int(n)
            if n >= 0:
                if n == 0:
                    return 0
                elif n == 1 or n == 2:
                    return 1
                else:
                    return fibonacci(n - 1) + fibonacci(n - 2)
            else:
                return "Input must be non-negative"
        except ValueError:
            return "Wrong type of input."

        n = int(input("Enter the value of n: "))
        print(fibonacci(n))


    if __name__ == "__main__":
        fibonacci()
