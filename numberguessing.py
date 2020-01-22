from random import randint

def startGame():
    numRand = numRandGenerate()
    guesses = []

    print("The computer has generated a number between 1 and 100, take a guess: ")

    # Get first guess, could use validation or create a function to get integer value.
    guess = int(input())

    while(guess != numRand):
        guesses.append(guess)

        # Incorrect guess gives you a hint, lets you guess again.
        if (guess > numRand):
            guess = int(input("Too high, next guess? "))
        else:
            guess = int(input("Too low, next guess? "))

    # Correct guess messages
    print("Congrats! You guessed the correct number:", numRand)
    print("It took you " + str(len(guesses)) + " guesses.")

# Function for generating a random number within a range.
def numRandGenerate():
    return randint(1, 100)

if __name__ == '__main__':
    startGame()