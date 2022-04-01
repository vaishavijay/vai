
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "John",
    "LastName": "Mortensen",
    "DOB": "October 21",
    "Residence": "San Diego",
    "Email": "jmortensen@powayusd.com",
    "Owns_Cars":["2015 Fusion","2011 Ranger","2003 Excursion","1997 F-350", "1969 Cadillac"]
})

InfoDb.append({
    "FirstName": "Sunny",
    "LastName": "Naidu",
    "DOB": "August 2",
    "Residence": "San Diego",
    "Email": "snaidu@powayusd.com",
    "Owns_Cars":["A","B","C"]
})

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)2  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion


if __name__=='__main__':
    # print_menu1()
    tester()