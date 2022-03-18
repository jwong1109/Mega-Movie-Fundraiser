# Start of loop

# Initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count != MAX_TICKETS:
    # Get details
    name = input("What's your name? ").title()
    count += 1
