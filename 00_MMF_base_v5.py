"""Added 03_age_validator_v4
"""

# Import Statements

# Functions go here


# Check that the ticket name is not blank
def not_blank(question):
    while True:
        response = input(question).title()
        if not response.isalpha():  # Ensures input contains at least 1 letter
            print("You can't leave this blank...")  # Error if not
        else:
            return response  # Otherwise return the input


# Checks for valid integer (eg for age)
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


# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before and
# show instructions if needed


# Loop to get ticket details
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count < MAX_TICKETS:
    if MAX_TICKETS - count > 1:
        print(f"\nThere are {MAX_TICKETS - count} tickets left")
    else:
        print(f"\n**** There is ONLY ONE ticket left! ****")
    # Get details
    name = not_blank("Enter ticket-holder's name: ")
    if name == "Xxx":
        break
    else:
        MINIMUM_AGE = 12
        MAXIMUM_AGE = 110
        age = number_checker(f"Please enter {name}'s age: ")
        if age < MINIMUM_AGE:
            print(f"Sorry, {name} is too young for this movie")
        else:
            while not age <= MAXIMUM_AGE:  # Age must be between 12 and 110
                age = number_checker(f"\nAt {age} {name} is very old. "
                                     f"Please re-enter {name}'s age: ")
            count += 1  # Don't want to include escape code in the count

if count < MAX_TICKETS:
    print(f"\n{count} tickets have now been sold")
    print(f"There are still {MAX_TICKETS - count} available")
else:
    print("\nAll the available tickets have been sold")
    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (an apply surcharge if required)

# Calculate total sales and profit

# Output data to text file
