Menu options in print statement
def print_menu1():
    print('1 -- Hot Coffee' )
    print('2 -- Cold Coffee' )
    print('3 -- Pastries' )
    print('4 -- Water' )

    print('5 -- Exit' )
    runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'Hot Coffee',
    2: 'Cold Coffee',
    3: 'Pastries',
    4: 'Water',
    5: 'Exit',
}

# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

# menu option 1
def one():
    print('Enjoy your \'Hot Coffee\'')

# menu option 2
def two():
    print('Enjoy your \'Cold Coffee\'')

# menu option 3
def three():
    print('Enjoy your \'Pastries\'')

def four():
    print('Enjoy your \'Water\'')

# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('What would you like to order today? (enter 1-7) '))
            if option == 1:
                one()
            elif option == 2:
                two()
            elif option == 3:
                three()
            elif option == 4:
                four()


            # Exit menu
            elif option == 7:
                print('Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 7.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    # print_menu1()
    print_menu2()