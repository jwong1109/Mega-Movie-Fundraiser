""" Calculate price based on age
This function will be used in conjunction with others to check that the
age is between 12 and 110
"""


def calculate_ticket_price(age):
    CHILD_AGE = range(12, 16)
    STANDARD_AGE = range(16, 65)
    RETIRED_AGE = range(65, 111)
    CHILD_PRICE = 7.5
    STANDARD_PRICE = 10.5
    RETIRED_PRICE = 6.5

    if age in CHILD_AGE:
        ticket_price = CHILD_PRICE
    elif age in STANDARD_AGE:
        ticket_price = STANDARD_PRICE
    else:
        ticket_price = RETIRED_PRICE
    return(ticket_price)


# Main routine
# temporary input statements - during development
name = input("Name: ")
age = int(input("Age: "))

print(f"The price is ${calculate_ticket_price(age):,.2f}")
