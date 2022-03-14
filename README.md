# Vaishavi Jayashankar, APCSP Period 5

### Table Of Contents:
Week | [1](https://github.com/vaishavijay/vaishavijay.github.io/edit/main/README.md#week-) | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11

# Week 1: 

### What can I do with Tech to improve mine or others education? 

I can use tech to hep organize resources to form positive concrete study habits, such as the Study Buddy website my team and I created last trimester for our PBL project.

## 5.1 TPT: Beneficial and Harmful Effects of Computing

**1. Come up with three of your own Beneficial and corresponding Harmful Effects of Computing**

Two advantages to computing are speed and accuracy in any procedure carried out by a program, piece of technology, etc, but this speed and accuracy depend highly on the procedures or processes used. If the procedure to carry out something is wrong, then the result will be wrong. This can be bad if you're using a procedure not knowing it was flawed and applying it to multiple parts of a program. This can also make technology very addicting as reward comes quicker, such as through video games, watching films, and social media. In addition, storage is much more efficient. However, this can be bad if data is not backed up somewhere such as an external drive, so lots of data have a risk of being lost, corrupted, or damaged.

**2. Talk about dopamine issues above. Real? Parent conspiracy? Anything that is impacting your personal study and success in High School?**

While there are many benefits to technology such as efficiency, speediness, and its ability being able to distract us from the waves of life, with this comes many negatives. Social media, video games, and other forms of quick consumable media are crafted by developers of apps and software designed to give users quick dopamine boosts such as instant content with a simple scroll, winning in games, etc. Thus, using technology instantly becomes very addicting which can distract students from school, which is extremely harmful in high school especially.

## 5.2 TPT: Digital Empowerment

**1. How does someone empower themself in a digital world?**

Someone can empower themselves in a digital world by bringing awareness to areas where technology is not as prominent in the world (rural areas, no wifi, not enough resources, etc) to build and support others.

**2. How does someone that is empowered help someone that is not empowered? Describe something you could do at Del Norte HS.**

Something someone who is empowered could do is help get any needed resources someone who is not empowered. At Del Norte HS, if someone does not have access to a personal device, for example, I could help them get a school chromebook and reccomend some places with free public wifi, depending on their needs and accessability. I could also help them get in contact with an adult in the school who can help them further with any assistance they may need.

**3. Is paper or red tape blocking digital empowerment? Are there such barriers at Del Norte? Elsewhere?**

Red tape blocking is digital empowerment because it encourages privacy, security, and online saftey so it is safe for everyone.

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

# Create Task

### Project - [4-Function Calculator](https://docs.google.com/document/d/1ihcfASxU-qed3BZCdALNmFjTqxmxcIAFpRq286g-K6c/edit?usp=sharing)

* Details - Running currently in project (Home -> Subject List -> Math Calculator) 

* [**Written Response**](https://docs.google.com/document/d/1-cEOgEqU7CdsWWhsyQlTJNcKnc2usHczHN845HUrJl4/edit)

* [**Create Task Video**](https://drive.google.com/file/d/1__l-X63cNrEr4FOH9hwNYXpQ8KkSDkqX/view?usp=sharing)

* [**Notes**](https://docs.google.com/document/d/1Avc5kdhr4JB_pN7sum7et9n1Zrrovus6btT_LmoVAKU/edit?usp=sharing)


## Create Task Guidelines

**Instructions For Input:**

* the User is going to be inputting functions to calculate by pressing buttons that correspond with certain numbers or calculative functions (i.e addition, subtraction, multiplication, division)

**Use of at least one list (or another collection type) to represent a collection of data that is stored and used to manage program complexity and help fulfill the program’s purpose**

* Calculations will be stored in an array

**At least one procedure that contributes to the program’s intended purpose, where you have defined: the procedure’s name, the return type (if necessary), one or more parameters, etc.**

* The procedure will take in user input and calculate integers. If a user is going to be typing in multiple numbers at a time, the procedure backs up each number into the form of a string so that the numbers don't add up to one another. This will allow the user to calculate larger numbers.

**An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure**

* It will use sequencing in the procedure since each piece of code happens one after another

**Calls To Your Student-Developed Procedure**

* will be a student-developed procedure that saves answers for calculation as a variable and by using arrays and multiple variables, the program will display the answers of the last 6 calculations the user makes

**Instructions for output (tactile, audible, visual, or textual) based on input and program functionality**

* Calculations will be displayed on the screen per calculation the user makes (visual output aka calculations that the user initiates)

