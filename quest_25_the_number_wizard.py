# This is a simple number guessing game where the user has to guess a secret number. The secret number is set to 5, and the user can keep guessing until they get it right. The program provides feedback on whether the guess is too low or too high.
secret_number = 5
# Start an infinite loop to allow the user to keep guessing until they guess the correct number
while True:
# Prompt the user to enter their guess
    guess = int(input("Guess the number: "))
# Check if the guess is correct, too low, or too high and provide feedback accordingly
    if guess == secret_number:
        print("Correct!")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")