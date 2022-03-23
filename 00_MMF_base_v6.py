"""Added 04_calculate_ticket_price_v4
Also includes total profit calculation in main routine.
Have changed the variable 'count' to 'ticket_count' and made the formatting
and language in the print statements easier to understand.
"""

# Import Statements

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


# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before and
# show instructions if needed


# Loop to get ticket details
MAX_TICKETS = 5
TICKET_COST_PRICE = 5.00

name = ""
ticket_count = 0
profit = 0

while name != "Xxx" and ticket_count < MAX_TICKETS:
    if MAX_TICKETS - ticket_count > 1:
        print(f"\nThere are {MAX_TICKETS - ticket_count} tickets left")
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
            ticket_count += 1  # Don't want to include escape code in the ticket_count

            # Calculate ticket price
            ticket_price = calculate_ticket_price(age)
            print(f"For {name}, the price is ${ticket_price:,.2f}")
            profit += (ticket_price - TICKET_COST_PRICE)

# Calculate total sales and profit
if ticket_count < MAX_TICKETS:
    if ticket_count > 1:  # Making sure it reads OK when only one ticket sold
        print(f"\n{ticket_count} tickets have now been sold")
    else:
        print("1 ticket has now been sold")
    if MAX_TICKETS - ticket_count > 1:
        print(f"{MAX_TICKETS - ticket_count} tickets are still available\n")
    else:
        print("1 ticket is still available\n")  # Making sure it reads OK when
        # only one ticket left
else:
    print("\n!!!!!!!! All the available tickets have now been sold !!!!!!!!")
    print("*" * 60)

print(f"Ticket profit is ${profit:.2f}")

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (an apply surcharge if required)


# Output data to text file
