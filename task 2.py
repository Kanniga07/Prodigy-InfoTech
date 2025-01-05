import random

def guess_the_number():
    print("'Guess the Number' welcomes you!")
    print("A number between 1 and 100 comes to mind.")
    print("Attempt to predict it!")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        guess = input("Put your guess here: ")

        if not guess.isdigit():
            print("The input is invalid. Enter a valid integer, please.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < target_number:
            print("Too low! Give it another go.")
        elif guess > target_number:
            print("Too high! Give it another go.")
        else:
            print(f"Well done! In the {attempts} attempts, you accurately guessed the number {target_number}.")
            guessed_correctly = True

if __name__ == "__main__":
    guess_the_number()
