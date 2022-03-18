"""Noticed the count is actually incorrect. In the previous version
the program was counting the XXX as a sold seat.
Also, further improvements on the emphasis - drawing the user's attention when
there is only one available seat left
"""

# Initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count < MAX_TICKETS:
    if MAX_TICKETS - count > 1:
        print(f"\nYou have {MAX_TICKETS - count} seats left")
    else:
        print(f"\n**** You have ONLY ONE seat left! ****")
    # Get details
    name = input("What's your name? ").title()
    if name != "Xxx":
        count += 1  # Don't want to include escape code in the count

if count < MAX_TICKETS:
    print(f"\nYou have sold {count} tickets")
    print(f"There are still {MAX_TICKETS - count} available")
else:
    print("\nYou have sold all the available tickets")
