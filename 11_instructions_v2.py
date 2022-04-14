"""This component is based on v1
Puts the component into it's own function
This version includes actual instructions
"""


# Function containing instructions
def show_instructions(valid_responses):
    instructions = ""
    while not instructions:
        instructions = not_blank("Would you like to read the "
                                 "instructions?: ").lower()
        instructions = (get_choice(instructions, valid_responses))

    if instructions == "Y":
        print("\n**********************************************************\n")
        print("**** Mega Movie Fundraiser Instructions ****\n"
              "\nYou will be shown how many tickets are still available\n"
              "for sale and asked for the first ticket-purchaser's name.\n"
              "You will then be asked to input the ticket-purchaser's age.\n"
              "\nThis is because:\n"
              "\t-the minimum age for entry is 12; and\n"
              "\t-there is a standard price for adults; but\n"
              "\t-different prices for students and retired people.\n"
              "\nThe program will then ask you for the snacks required\n"
              "and once these are entered you will then need to provide a\n"
              "valid method of payment.\n"
              "\nThis process keeps repeating until either all tickets are\n"
              "sold or you choose to exit the program.\n"
              "\nOn exit, a summary of sales and profits will be printed to\n"
              "the screen. Full details of all sales and profits are also \n"
              "output to .csv files. These can be found in the same\n"
              "directory in which the program is stored.\n")
        print("**********************************************************\n")
    print("Program launches...")


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
show_instructions(valid_yes_no)
