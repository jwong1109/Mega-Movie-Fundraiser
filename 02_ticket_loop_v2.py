"""This version includes a print statement at the start, saying how many
tickets are still available for sale
"""

# Initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count != MAX_TICKETS:
    print(f"You have {MAX_TICKETS - count} seats left")
    # Get details
    name = input("What's your name? ").title()
    count += 1

if count < MAX_TICKETS:
    print(f"You have sold {count} tickets")
    print(f"There are still {MAX_TICKETS - count} available")
else:
    print("You have sold all the available tickets")
