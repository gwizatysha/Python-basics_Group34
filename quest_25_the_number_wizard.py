secret_number = 5

while True:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct!")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")