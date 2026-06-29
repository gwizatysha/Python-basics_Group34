for number in range(1, 101):
    
    # If the number is divisible by both 3 and 5 print FizzBuzz
    # We check this first before checking 3 or 5 alone
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

  # If the number is only divisible by 3 print Fizz
    elif number % 3 == 0:
        print("Fizz")
    
    # If the number is only divisible by 5 print Buzz
    elif number % 5 == 0:
        print("Buzz")

    # If none of the above just print the number itself
    else:
        print(number)