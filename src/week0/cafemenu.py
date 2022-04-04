print("Welcome to the Café! What would you like to order?")
def print_menu1():
    print('Hot Coffee' )
    print('Iced Coffee' )
    print('Pastries' )
    print('Exit ' )
    runOptions()


menu_options = {
    1: 'Hot Coffee',
    2: 'Iced Coffee',
    3: 'Pastries',
    4: 'Exit',
}

def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

def hot():
    print('You chose \'Hot Coffee\'')

def cold():
    print('You chose \'Iced Coffee\'')

def past():
    print('You chose \'Pastries\'')


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
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


if __name__=='__main__':
    # print_menu1()
    print_menu1()
