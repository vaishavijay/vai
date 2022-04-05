
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
    recursive_loop()  # requires initial index to start recursion


if __name__ == "__main__":
    driver()