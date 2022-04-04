"""Testing if the first or second character in a string is a number.
In the program all I have done is to try an alternative method
of splitting the first 1 or 2 characters off from the rest of the string
"""

test_strings = [
    "Popcorn",  # String with no number
    "2 pc",  # String with a space then valid number
    "1.5OJ",  # String with a preceding decimal
    "4OJ",  # String with preceding integer but no space
    "12Chips"
    ]

for item in test_strings:
    if item[0].isdigit():  # Tests to see if first char is a digit
        if item[1].isdigit():  # If so, what about the second chzr
            quantity = int(item[0]+item[1])
            snack = item[2:]  # and split the rest of the string off at item 2
        else:
            quantity = int(item[0])  # If only the first char is a digit
            snack = item[1:]
    else:  # If no digit is found
        quantity = 1
        snack = item
    print(f"Quantity = {quantity}")
    print(f"Snack = {snack}")
