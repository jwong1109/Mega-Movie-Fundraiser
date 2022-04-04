"""Moved the check of sales against the maximum tickets into its own function
Added lists to hold ticket holder's name and the price paid for their ticket
Added a dictionary to get data from these 2 new lists
Added code to append name and ticket price to the new lists (line 137 and 138)
Added the import re and import panda libraries (installing panda package if
necessary)
Added the print statement for ticket profit on line 162
Modified the 'else' statements under 'if MAX_TICKETS - ticket_count > 1:'
to improve flow and readability
Added the print details (movie_frame: bottom 3 lines) which uses the pandas
library to create a printable DataFrame based on the dictionary
"""

# Import Statements
import re
import pandas  # Might need to install pandas if library does not already exist
# Functions go here


# Calculate the ticket price (based on given age)
def calculate_ticket_price(age):
    # Ages - anything over standard age must qualify for retired price
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if age in child_age:
        price = child_price
    elif age in standard_age:
        price = standard_price
    else:
        price = retired_price

    return price


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


def check_max_tickets(maximum, sold):
    if maximum - sold > 1:
        print(f"\nThere are {maximum - sold} tickets left")
    else:
        # Warns user there is only one seat left
        print(f"\n**** There is ONLY ONE ticket left! ****")


def check_valid_age(minimum, maximum):
        age = number_checker(f"Please enter {name}'s age: ")
        if age < minimum:
            print(f"Sorry, {name} is too young for this movie")
            return None
        else:
            while not age <= maximum:  # Age must be between 12 and 110
                age = number_checker(f"\nAt {age} {name} is very old. "
                                     f"Please re-enter {name}'s age: ")
            return age


# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data
all_names = []
all_tickets = []


# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

MINIMUM_AGE = 12
MAXIMUM_AGE = 110
MAX_TICKETS = 5
TICKET_COST_PRICE = 5.00
name = ""
ticket_count = 0
profit = 0


# Ask user if they have used the program before and
# show instructions if needed


# Loop to get ticket details
# Initialise loop so that it runs at least once

while name != "Xxx" and ticket_count < MAX_TICKETS:
    # Check to ensure there are still tickets left
    check_max_tickets(MAX_TICKETS, ticket_count)

    # Get details
    # Get name
    name = not_blank("Enter ticket-holder's name: ")
    if name == "Xxx":
        break
    else:
        # Checks for a valid age and then calculate ticket price
        age = check_valid_age(MINIMUM_AGE, MAXIMUM_AGE)
        if not age:
            continue  # Restarts the get ticket loop
        else:
            ticket_count += 1  # Don't want escape code in the ticket_count

        # Calculate ticket price
        ticket_price = calculate_ticket_price(age)
        print(f"For {name}, the price is ${ticket_price:,.2f}")
        profit += (ticket_price - TICKET_COST_PRICE)

        # Add name and ticket price to lists
        all_names.append(name)
        all_tickets.append(ticket_price)

        # Get snacks

        # Ask for payment method (an apply surcharge if required)

    # End of tickets/snacks/payment loop

# Calculate total sales and profit
if ticket_count < MAX_TICKETS:
    if ticket_count > 1:  # Making sure it reads OK when only one ticket sold
        print(f"\n{ticket_count} tickets have now been sold")
    else:
        print("1 ticket has now been sold")
    if MAX_TICKETS - ticket_count > 1:
        print(f"{MAX_TICKETS - ticket_count} tickets are still available")
    else:
        print("1 ticket is still available\n")  # Making sure it reads OK when
        # only one ticket left
else:
    print("\n!!!!!!!! All the available tickets have now been sold !!!!!!!!")
    print("*" * 60)

# Print details
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)
print(f"Ticket profit is ${profit:.2f}")


    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (an apply surcharge if required)


# Output data to text file
