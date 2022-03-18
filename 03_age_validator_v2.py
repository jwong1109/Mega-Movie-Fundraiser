""" Integer checking function - loops until a valid number is entered
This version uses 'isinstance()' to validate the integer and cuts down on
the number of parameters required in the function by incorporating the valid
age range into a loop in the main routine
"""


def number_checker(text):
    valid = False
    while not valid:
        # asking user for a number and check to see if it is valid:
        try:
            number_to_check = int(input(text))
            if isinstance(number_to_check, int):
                valid = True
                return number_to_check
        except ValueError:
            print("\nPlease enter an integer (i.e. a whole number "
                  "with no decimals)")


# Main Routine
# Check for a valid age - must be between 12 and 110
age = number_checker("\nPlease enter the age of the ticket-holder: ")
while not 12 <= age <= 110:
    age = number_checker("\nPlease enter an integer between 12 and 110: ")
print(f"Age = {age}")
