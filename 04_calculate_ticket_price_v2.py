""" Calculate price based on age - v2
Don't need "RETIRED AGE" constant because it can be inferred
"""


def calculate_ticket_price(age):
    CHILD_AGE = range(12, 16)
    STANDARD_AGE = range(16, 65)

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
