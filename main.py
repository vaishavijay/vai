from src.week0 import animation, matrix, cafemenu, swap
from src.week1 import fibonacci, listsnloops
from src.week2 import factorial, lcm

main_menu = []
math_menu = [
    ["Number Swap", swap.swap],
    ["Matrix", matrix.matrix],
    ["Fibonacci", fibonacci.fibonacci],
    ["Factorial", factorial.factorial],
    ["LCM Calculator", lcm.lcm]
]

patterns_menu = [
    ["Cafe Menu", cafemenu.print_menu1],
    ["Pyramid Animation", animation.pyramid],
]

data_menu = [
    ["For Loop", listsnloops.for_loop],
    ["While Loop", listsnloops.while_loop],
    ["Recursive Loop", listsnloops.recursive_loop0],
]

# Menu banner is typically defined by menu owner
border = "=" * 20
banner = f"\n{border}\n Please Select An Option \n{border}"


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", math_menu])
    menu_list.append(["Patterns", patterns_menu])
    menu_list.append(["Data", data_menu])
    buildMenu(title, menu_list)


def math_menu():
    title = "Math Submenu" + banner
    buildMenu(title, math_menu)


def patterns_menu():
    title = "Patterns Submenu" + banner
    buildMenu(title, patterns_menu)


def data_menu():
    title = "Data Submenu" + banner
    buildMenu(title, data_menu)

def buildMenu(banner, options):
    print(banner)
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
