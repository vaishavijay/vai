# Vaishavi Jayashankar

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

## Data Structures Project

Link to notes: __________
Data Structures Project: https://replit.com/@vaishavijay/Cafe-Menu
* Café Menu: (allows user to choose between drinks and pastries)
* Boat Animation: https://replit.com/@vaishavijay/vaishavijay#main.py

Code Snippets + Learnings: 
      print("Welcome to the Café! What would you like to order?")
        def print_menu1():
             print('Hot Coffee' )
            print('Iced Coffee' )
           print('Pastries' )
           print('Exit ' )
            runOptions()

(Prints out options)

def hot():
    print('You chose \'Hot Coffee\'')

def cold():
    print('You chose \'Iced Coffee\'')

def past():
    print('You chose \'Pastries\'')

(Defines variables)

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
(Choice menu)

        if __name__=='__main__':
           # print_menu1()
            print_menu2()

Allows code/menu to run overall

