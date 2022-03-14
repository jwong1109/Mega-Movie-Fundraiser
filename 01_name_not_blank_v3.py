# Check Name Function
def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("You can't leave this blank...")
        else:
            return response


# ******** Main Routine ********
name = not_blank("What's your name? ", )
