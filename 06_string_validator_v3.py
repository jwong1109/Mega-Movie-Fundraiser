"""Based on 06_string_validator_v2, this program includes the yes and no
checker from 05_yes_no_checker_v3. This program uses the string validator
function to ask if the user wants to order snacks. If the response is 'yes'
the function is called repeatedly to check that the choice of snacks is valid.
The user chooses 'x' to stop ordering snacks
"""


def get_choice(question, valid_choices):
    choice_error = "Sorry, that is not a valid choice"

    choice = input(question).lower()
    for item in valid_choices:
        if choice in item:
            choice = item[0].title()
            return choice

    print(choice_error)
    return get_choice(question, valid_choices)


# Main Routine

# Order snacks - question and choices
valid_yes_no_responses = ["y", "yes", "n", "no"]
check_snacks = "Would you like snacks? "

# Asks for snacks - question and choices
ask_for_snacks = "What snack do you want - 'x' to stop ordering: "
valid_snacks = [["popcorn", "p", "corn", "1"], ["m&ms", "mms", "m", "2"],
                ["pita chips", "chips", "pc", "pita", "c", "3"],
                ["water", "w", "4"], ["x", "exit", "5"]]

# Process for ordering snacks
getting_snacks = True
snacks_required = get_choice(check_snacks, valid_yes_no_responses)
while getting_snacks:
    if snacks_required == "N":
        print("You don't want snacks")
        getting_snacks = False
    else:
        snack = get_choice(ask_for_snacks, valid_snacks)
        if snack != "X":
            print(f"You have chosen {snack}")
        else:
            getting_snacks = False
            print("Thanks for ordering your snacks")
