# This is a simple text-based adventure game. The player makes choices that lead to different endings.
def start():
    print("\nYou are hungry. You walk into the kitchen.")
    print("1 = Make a sandwich")
    print("2 = Look in the fridge")

# Prompt the player for their choice    
    choice = input("Choose 1 or 2: ")
    
    if choice == "1":
        sandwich()
    else:
        fridge()

# Define the sandwich function that handles the sandwich-making scenario
def sandwich():
    print("\nYou make a ham sandwich. It looks good.")
    print("1 = Eat it now")
    print("2 = Save it for later")
    
    # Prompt the player for their choice
    choice = input("Choose 1 or 2: ")
    # Depending on the player's choice, print the corresponding ending
    if choice == "1":
        print("\n ENDING 1: You eat the sandwich. You are happy!")
    else:
        print("\n ENDING 2: Your dog finds the sandwich first and eats it")

def fridge():
    print("\n ENDING 3: You find an apple in the fridge. It tastes great.")
# Start the game by calling the start function
start()