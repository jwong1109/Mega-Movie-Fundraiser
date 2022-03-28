"""Based on 06_string_validator_v1, this program makes the function more
flexible by using generic variable names - so that it can be used to check
for valid choices from any list
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
# temporary input statement - during development
ask_for_snacks = "What snack do you want: "
valid_snacks = [["popcorn", "p", "corn", "1"], ["m&ms", "mms", "m", "2"],
                    ["pita chips", "chips", "pc", "pita", "c", "3"],
                    ["water", "w", "4"]]
for test in range(6):
    print(f"You want {get_choice(ask_for_snacks, valid_snacks)}")
