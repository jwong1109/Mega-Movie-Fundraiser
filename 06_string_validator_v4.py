"""Based on 06_string_validator_v3, this program keeps a list of all valid
orders.
The user chooses 'x' to stop ordering snacks.
Does not yet include an easy option to order more than one of any snacks.
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

# Order snacks - question
check_snacks = "Do you want snacks? " # Asks if the user wants to order any

# Valid options for yes/no questions
valid_yes_no_responses = ["y", "yes", "n", "no"]

# Asks for snacks - question
ask_for_snacks = "What snack do you want - 'x' to stop ordering: "

# Valid snacks holds list of all snacks. Each item is itself a list with all
# the acceptable input options for each snack - full name, initials and
# abbreviations, as well as reference number
valid_snacks = [["popcorn", "p", "corn", "1"], ["m&ms", "mms", "m", "2"],
                ["pita chips", "chips", "pc", "pita", "c", "3"],
                ["water", "w", "4"], ["x", "exit", "5"]]

# Process for ordering snacks

# Firstly, find out whether the user wants to order snacks
# Call the generic string checking function with the 'check_snacks' question
# and the list of valid yes/no responses as parameters
snacks_required = get_choice(check_snacks, valid_yes_no_responses)

# The snack_order list records the complete order for a single user
snack_order = []

# Assumption that every user will want to order snacks
getting_snacks = True
while getting_snacks:
    if snacks_required == "N":  # but if they don't want any snacks
        getting_snacks = False  # break the while loop
    else:
        # Otherwise, for each snack, the generic string checker is called with
        # the 'ask_for_snacks' question and the list of valid snacks as
        # parameters
        chosen_snack = get_choice(ask_for_snacks, valid_snacks)
        if chosen_snack != "X":  # Check response isn't the escape key
            # and if not, add the item to the 'snack_order' list
            snack_order.append(chosen_snack)
        else:  # Otherwise, it must be the escape key so end the loop
            getting_snacks = False

# After the loop is broken, check for an empty list
if len(snack_order) > 0:  # If there is something in the list, print each item
    print("\nThis is a summary of your order: ")
    for item in snack_order:
        print(f"\t{item}")
else:  # Otherwise, print this
    print("No snacks were ordered")
