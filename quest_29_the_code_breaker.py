secret_code = 42
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}/3 - Enter the secret code: "))

    if guess == secret_code:
        print("Access Granted!")
        break
    else:
        print("Incorrect code.")

if guess != secret_code:
    print("Access Denied. Too many failed attempts.")