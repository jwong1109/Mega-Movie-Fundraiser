""" 4th iteration of the integer checking function
Wanted to limit the possibility of getting a false age for children < 12
This means creating upper and lower age limits as constants
"""


def number_checker(question):
    number = ""
    while not number:
        # asking user for a number and check to see if it is valid:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("\nPlease enter an integer (i.e. a whole number "
                  "with no decimals)")


# Main Routine
# Check for a valid age
MINIMUM_AGE = 12
MAXIMUM_AGE = 110
age = number_checker("\nPlease enter the age of the ticket-holder: ")
if age < MINIMUM_AGE:
    print("Sorry, you are too young for this movie")
else:
    while age <= MAXIMUM_AGE:  # Age must be between 12 and 110
        age = number_checker("\nPlease enter an integer between 12 and 110: ")
    
print(f"Age = {age}")
