firstNumber = int(input("Please enter your first number : "))
secondNumber = int(input("Please enter the second number : "))
mathOperation = input ("Please enter the operation (ex: add , subtract , multiply , divide)")
def calculator (a,b,operation) :
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


calculator(firstNumber,secondNumber,mathOperation)