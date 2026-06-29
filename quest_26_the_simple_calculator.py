# This is a simple calculator program that takes two numbers and an operation as input from the user, performs the specified operation, and prints the result. The supported operations are addition, subtraction, multiplication, and division.
firstNumber = int(input("Please enter your first number : "))
secondNumber = int(input("Please enter the second number : "))
mathOperation = input ("Please enter the operation (ex: add , subtract , multiply , divide)")
# The calculator function takes two numbers and an operation as input, performs the specified operation, and prints the result. The supported operations are addition, subtraction, multiplication, and division. If the user enters an invalid operation, it will print "Invalid operation choice".
def calculator (a,b,operation) :
    # Check which operation the user has chosen and perform the corresponding calculation
    if operation == "add":
        print(f'{a+b}')
    elif operation == "subtract":
        print (f'{a-b}')
    elif operation == "multiply":
        print (f'{a*b}')
    elif operation == "divide":
        print(f'{a/b}')
    else :
        print( "Invalid operation choice")

# Call the calculator function with the user's input
calculator(firstNumber,secondNumber,mathOperation)