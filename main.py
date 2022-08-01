# Imports
import os
from handler.remover import remover

# Vars for main loop
start_menu = ["Set Path",
              "Set Extension",
              "Add Keyword(s)",
              "Remove Keyword(s)",
              "Verify Information",
              "Start Removal",
              "Exit"]

# Main loop
keep_removing = True
r = remover()  # Initialize class before looping
while (keep_removing):
    error_msg = ""

    # Draw the menu for the user
    for i, menu in enumerate(start_menu):
        if i == len(start_menu) - 1:
            print("0.", menu)
        else:
            print(f"{i+1}.", menu)

    # Allow the user to select an option
    user_input = input(f"Select your option [0 - {len(start_menu)-1}]: ")

    # Then filter the entered response, as it must be an integer
    if user_input.isnumeric():
        if int(user_input) in range(0, len(start_menu)):
            remember_choice = int(user_input)
        else:
            error_msg = ("Invalid entry, please enter a number between 0"
                         f"and {len(start_menu)-1}")
    else:
        error_msg = "Invalid entry, please enter a number"

    # If the entry is valid, we perform an action
    if not error_msg:
        if int(user_input) == 0:
            keep_removing = False
        elif int(user_input) == 1:
            error_msg = r.set_path()
        elif int(user_input) == 2:
            error_msg = r.set_extension()
        elif int(user_input) == 3:
            r.add()
        elif int(user_input) == 4:
            r.remove()
        elif int(user_input) == 5:
            r.printAll()
            error_msg = r.find_match()
        elif int(user_input) == 6:
            error_msg = r.execute()

    if error_msg:
        print(error_msg)
        # Then pause so user can see msg before cls
        input("Press enter to continue...")

    # Wipe the command line after all is done and repeat
    os.system('cls')

quit()
