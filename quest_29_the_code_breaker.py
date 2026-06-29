# This is a simple code-breaking game where the user has to guess a secret code within a limited number of attempts. The secret code is set to 42, and the user has 3 attempts to guess it correctly. If the user guesses the code correctly, they are granted access; otherwise, they are denied access after exhausting their attempts.
secret_code = 42
max_attempts = 3
# Loop through each attempt
for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}/3 - Enter the secret code: "))
# Check if the guess is correct
    if guess == secret_code:
        print("Access Granted!")
        break
    else:
        print("Incorrect code.")
# If the user has used all attempts and still hasn't guessed the code, print access denied message
if guess != secret_code:
    print("Access Denied. Too many failed attempts.")