"""This component provides the opportunity for new users to find out how the
program is supposed to work
"""


# Function containing instructions
def show_instructions():
    print("**** Mega Movie Fundraiser Instructions ****\n"
          "Instructions go here. They are brief but helpful\n")


# Function takes the entered choice and list of valid choices as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


# Check that the ticket name is not blank
def not_blank(question):
    while True:
        response = input(question).title()
        if not response.isalpha():  # Ensures input contains at least 1 letter
            print("You can't leave this blank...")  # Error if not
        else:
            return response  # Otherwise return the input


# Main routine
# Valid options for any yes/no questions
valid_yes_no = [["y", "yes"], ["n", "no"]]

instructions = ""
while not instructions:
    instructions = not_blank("Would you like to read the instructions?: ").lower()
    instructions = (get_choice(instructions, valid_yes_no))

if instructions == "Y":
    show_instructions()

print("Program launches...")
