"""Based on 00_MMF_base_v11
Took ticket price out of the snack calculation
and added it back in as part of the subtotal
Summary information regarding profits will be in a separate data frame so I
created a series of new lists (to populate new summary_data_dict) after
"surcharge_mult_list = []"
Added the summary_frame (after the movie_frame) which includes the calculation
of snack totals and profits.
Created a constant to hold SNACK_PROFIT_MARGIN
Moved ticket_profit calculation down under summary_data calculations and
changed the name from profit to ticket_profit
Calculated total_profit as snack_profit + ticket_profit and added it into the
summary_data list
"""

# Import Statements
import re
import pandas  # Might need to install pandas if library does not already exist
# Functions go here


# This function splits snacks into quantity and snack name
# It has to be called before the snack (name) can be evaluated against the
# valid_snacks list
def split_order(choice):
    # Regular expression to test and find out if an item starts with a number
    number_regex = "^[1-9]"

    # If item has a number, separate the item into two: number and item
    if re.match(number_regex, choice):
        quantity_required = int(choice[0])
        snack_name = choice[1:]

    # If item has no number, assume number required is 1
    else:
        quantity_required = 1
        snack_name = choice

    # Need to remove white space from around snack
    snack_name = snack_name.strip()
    return quantity_required, snack_name


# Function takes the entered choice and list of valid choices as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


# Function to collate each order
def collate_order():
    # Valid snacks holds list of all snacks. Each item is itself a list with
    # all the acceptable input options for each snack - full name, initials and
    # abbreviations, as well as reference number
    valid_snacks = [["popcorn", "p", "corn", "(1"], ["m&ms", "mms", "m",
                                                     "mm", "(2"],
                    ["pita chips", "chips", "pc", "pita", "c", "(3"],
                    ["water", "w", "(4"], ["orange juice", "oj", "(5"],
                    ["x", "exit", "(6"]]

    # Valid options for yes/no questions
    valid_yes_no_responses = ["y", "yes", "n", "no"]

    # The snack_order list records the complete order for a single user
    snack_order = []
    # Maximum number of any snack item which can be ordered
    max_number_of_snacks = 4
    # Assumption that every user will want to order snacks
    getting_snacks = True
    while getting_snacks:
        snacks_required = ""
        while snacks_required != "N" and snacks_required != "Y":
            # Response is passed to the generic string checking function with
            # the list of valid yes/no responses as parameters
            check_snacks = input("Do you want snacks? (Y/N): ").lower()
            snacks_required = get_choice(check_snacks, valid_yes_no_responses)

        if snacks_required == "N":  # but if they don't want any snacks
            getting_snacks = False  # break the while loop
            break

        else:
            # Otherwise, for each snack, the generic string checker is called
            # with the 'ask_for_snacks' question and the list of valid snacks
            # as parameters
            option = ""
            while option != "X":
                snack = input("What snack do you want - 'x' to stop "
                              "ordering: ").lower()
                snack = split_order(snack)
                quantity = snack[0]
                if quantity > max_number_of_snacks:
                    snacks = None
                    print("Sorry, the maximum number you can order is 4")
                else:
                    snack = snack[1]
                    option = get_choice(snack, valid_snacks)
                    if option == "X":
                        getting_snacks = False
                    elif option is not None:  # Filters out invalid choices
                        snack_order.append([quantity, option])
    return snack_order


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


def check_valid_payment_method():
    ask_payment_method = input("How do you want to pay: ").lower()
    valid_payment_method = [["credit card", "card", "credit", "cc", "cr", "1"],
                            ["eftpos", "eft", "pos", "ep", "e", "2"],
                            ["cash", "ca", "money", "notes", "coins", "c", "3"]]
    payment_method = get_choice(ask_payment_method, valid_payment_method)
    return payment_method

# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data
all_names = []
all_tickets = []

# Creates separate list for each snack type
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

# Put the separate lists above into a master list
snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Store surcharge multiplier
surcharge_mult_list = []

# Lists to store summary data
# Heading order matches the lists in the 'snacks_lists' master list above
summary_headings = ["Popcorn", "M&Ms", "Pita Chips", "Water", "Orange Juice",
                    "Snack Profit", "Ticket Profit", "Total Profit"]

# Empty list to hold the data for above summary
summary_data = []

# Dictionary to hold summary information
summary_data_dict = {
    "Item": summary_headings,
    "Amount": summary_data
}

# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    "Popcorn": popcorn,
    "Water": water,
    "Pita Chips": pita_chips,
    "M&Ms": mms,
    "Orange Juice": orange_juice,
    "Surcharge Multiplier": surcharge_mult_list
}

# Cost of each snack
price_dict = {
    "Popcorn": 2.5,
    "Water": 2,
    "Pita Chips": 4.5,
    "M&Ms": 3,
    "Orange Juice": 3.25
}
SNACK_PROFIT_MARGIN = .2
SURCHARGE_RATE = .05
MINIMUM_AGE = 12
MAXIMUM_AGE = 110
MAX_TICKETS = 5
TICKET_COST_PRICE = 5.00
name = ""
ticket_count = 0
ticket_profit = 0
surcharge = 0


# Ask user if they have used the program before and
# show instructions if needed


# Loop to get ticket details
# Initialise loop so that it runs at least once

while name != "X" and ticket_count < MAX_TICKETS:
    # Check to ensure there are still tickets left
    check_max_tickets(MAX_TICKETS, ticket_count)

    # Get details
    # Get name - name can't be blank
    name = not_blank("Enter ticket-holder's name: ").title()
    if name == "X":
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

        # Add name and ticket price to lists
        all_names.append(name)
        all_tickets.append(ticket_price)

        # Get snacks
        snack_order = collate_order()

        # Assume no snacks have been bought
        for item in snack_lists:
            item.append(0)  # add 0 as the amount for each item

        # print(snack_order)
        for item in snack_order:  # The item only has 2 parts - number and snack
            if len(item) > 0:  # Checking to eliminate any blank orders
                to_find = item[1]  # Gets the snack name for the item ordered
                amount = item[0]
                add_list = movie_data_dict[to_find]  # Matches the snack name to
                # the snack_menu_dict
                add_list[-1] = amount  # Appends the number ordered to the end of
                # the dictionary list of quantities ordered eg if the most recent
                # quantity is 3, it would be added to the end of
                # this list: [2, 5, 0, 1, 3]

        # After the loop is broken, check for an empty list
        if len(snack_order) > 0:  # If there is something in the list,
            # print each item
            print("\nThis is a summary of your order: ")
            for item in snack_order:
                print(f"\t{item[0]} {item[1]}")
        else:  # Otherwise, print this
            print("No snacks were ordered")
        # Ask for payment method (an apply surcharge if required)
        payment_method = check_valid_payment_method()
        if not payment_method:
            continue

        elif payment_method == "Credit Card":
            surcharge_multiplier = SURCHARGE_RATE

        else:
            surcharge_multiplier = 0

        surcharge_mult_list.append(surcharge_multiplier)
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
print()

# Print details
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index("Name")  # Changes the index to reference
# the names rather than an actual index number

# Calculate the collective price of snacks ordered
movie_frame["Snack Cost"] = \
    movie_frame["Popcorn"] * price_dict["Popcorn"] + \
    movie_frame["Water"] * price_dict["Water"] + \
    movie_frame["Pita Chips"] * price_dict["Pita Chips"] + \
    movie_frame["M&Ms"] * price_dict["M&Ms"] + \
    movie_frame["Orange Juice"] * price_dict["Orange Juice"]

movie_frame["Sub Total"] = movie_frame["Snack Cost"] + movie_frame["Ticket"]

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + movie_frame["Surcharge"]

# Shorten column names
movie_frame = movie_frame.rename(columns={"Orange Juice": "OJ",
                                          "Pita Chips": "Chips",
                                          "Surcharge Multiplier": "SM"})

# Set up summary data frame
# Populate snack items from the master snack_lists
for item in snack_lists:
    # Sum items in each value list
    summary_data.append(sum(item))

# Get snack profit
# Get snack total from panda
snack_total = movie_frame["Snack Cost"].sum()
snack_profit = snack_total + SNACK_PROFIT_MARGIN
summary_data.append(snack_profit)

# Work out total profit and add to list
total_profit = snack_profit + ticket_profit
summary_data.append(total_profit)

# Force all columns to be printed
pandas.set_option("display.max_columns", None)

# Display numbers to 2 decimal places
pandas.set_option("display.precision", 2)

print(movie_frame)

# For testing purposes, ask user if they want to see all columns
# If not, just print Ticket, Sub Total, Surcharge, and Total columns
print_all = input("Print all columns? (Y for yes) :").upper()
if print_all == "Y":
    print(movie_frame)
else:
    print(movie_frame[["Ticket", "Snack Cost", "Sub Total", "Surcharge",
                       "Total"]])

print()



# Output data to text file
