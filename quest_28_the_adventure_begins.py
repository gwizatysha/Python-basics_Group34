def start():
    print("\nYou are hungry. You walk into the kitchen.")
    print("1 = Make a sandwich")
    print("2 = Look in the fridge")
    
    choice = input("Choose 1 or 2: ")
    
    if choice == "1":
        sandwich()
    else:
        fridge()

def sandwich():
    print("\nYou make a ham sandwich. It looks good.")
    print("1 = Eat it now")
    print("2 = Save it for later")
    
    choice = input("Choose 1 or 2: ")
    
    if choice == "1":
        print("\n ENDING 1: You eat the sandwich. You are happy!")
    else:
        print("\n ENDING 2: Your dog finds the sandwich first and eats it")

def fridge():
    print("\n ENDING 3: You find an apple in the fridge. It tastes great.")

start()