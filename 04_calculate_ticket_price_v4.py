""" Calculate price based on age - testing
Includes profit calculation
"""


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


# Main routine
# loop for testing purposes:
TICKET_COST_PRICE = 5.00
test_cases = [["Rangi", 15], ["Manaia", 16], ["Talia", 64], ["Arihi", 65]]
profit = 0

for test in test_cases:
    test_name = test[0]
    test_age = test[1]
    ticket_price = calculate_ticket_price(test_age)
    print(f"For {test_name},the price is ${ticket_price:,.2f}")
    profit += (ticket_price - TICKET_COST_PRICE)
print(f"\nProfit is ${profit:,.2f}")
