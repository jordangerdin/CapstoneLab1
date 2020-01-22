# Get number of classes
numClass = input("How many classes are you taking this semester? ")

# Initalize array
classList = []

# Read in all classes being taken
for i in range(int(numClass)):
    className = input("What is your #" + str(i + 1) + " class? ")
    classList.append(className)

# Print all classes in list
print("\nThe classes you are taking this semester are: ")
for course in classList:
    print(course)