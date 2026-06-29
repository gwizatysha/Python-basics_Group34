#The Potion Brewer

scales = int(input("How many dragon scales? "))
tears = int(input("How many elf tears? "))

total_cost = (scales * 10) + (tears * 3)
print(f"The potion costs {total_cost} gold to brew!")