"""This version checks to see if there is only ONE ticket left and, if so,
produces a more appropriately worded print statement. The spacing and the
readability of the output is also improved.
"""

# Initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count < MAX_TICKETS:
    if MAX_TICKETS - count > 1:
        print(f"\nYou have {MAX_TICKETS - count} seats left")
    else:
        print(f"\nYou have ONLY ONE seat left!")
    # Get details
    name = input("What's your name? ").title()
    count += 1

if count < MAX_TICKETS:
    print(f"\nYou have sold {count} tickets")
    print(f"There are still {MAX_TICKETS - count} available")
else:
    print("\nYou have sold all the available tickets")
