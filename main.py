import src.week0.animation
import src.week0.cafemenu
import src.week0.matrix
import src.week0.swap
import src.week1.infodb
import src.week2.lcm

main_menu = []
mathmenu = [
    ["Number Swap", src.week0.swap.swap],
    ["Matrix", src.week0.matrix.matrix],
    ["LCM Calculator", src.week2.lcm.lcm]
]

patternsmenu = [
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
    buildMenu(title, mathmenu)


def patterns_menu():
    title = "Patterns Submenu" + banner
    buildMenu(title, patternsmenu)


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
