""" Yes/No Checker
This component asks for a Yes/No response and keeps asking until
a valid response is provided
"""

error_message = "Please answer 'Y' or 'N'"
valid_responses = ["y", "yes", "n", "no"]
response = input("Do you want snacks? ").lower()
while response not in valid_responses:
    print(error_message)
    response = input("Do you want snacks? ").lower()

if response == "n" or response == "no":
    print("Valid answer. You don't want snacks")
else:
    print("Valid answer, You do want snacks")
