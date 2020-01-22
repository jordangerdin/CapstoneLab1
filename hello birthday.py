# Ask for users name
name = input("What is your name? ")
print("Hello", name)
print()

# Ask for users birthday
birthdayMonth = input("What month were you born in? ")

# Some print statements based on the inputs
print("Your name has " + str(len(name)) + " letters in it.")

# Small check to ignore case in typing of month.
if (birthdayMonth.lower() == "january"):
    print("Happy Birthday Month!")
else:
    print("You have entered: ", birthdayMonth)
