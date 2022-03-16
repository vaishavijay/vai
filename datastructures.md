[Test Prep](https://vaishavijay.github.io/testprep) | [Data Structures](https://vaishavijay.github.io/datastructures) | [Create Task](https://vaishavijay.github.io/createtask)

# Data Structures Project

### Notes: 

The digital divide is the name of the divide between differing access to the internet across socioeconomic, geographic, or demographic regions, such as between developing and first world countries. Some places have limited access to computers and websites. The internet may be used to protect and advocate for the government in these places. This divide affects both individuals and groups, and raises equity issues. 

Computing biases are biases written into computer code that can reflect the biases of the programmer. These biases can be embedded into any layer of software development. Programmers should take action to avoid introducing these biases whenever possible. This can include gearing towards a particular audience, or Netflix biasing towards showing their own shows.
Crowdsourcing is the process of enlisting the service of the crowd, large numbers of people, with or without notifying them. This could be things such as getting data from large amounts of people, or citizen science projects where many many people collaborate. 
Computers can raise legal or ethical concerns regarding copyright.
User data must be stored securely.

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

