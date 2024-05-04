import pandas as pd

# Convert the excel sheet into a database
df = pd.read_excel("Lorcana Card Database.xlsx")

while(True):
    print("\n 1. Add cards\n 2. Search cards\n 3. Remove cards\n 4. Quit\n")
    choice = input("What would you like to do: ")
    print(choice)
    if choice == "1":
        while(True):
            num = input("Card Number: ")
            exp = input("Expansion Number: ")
            print("\n 1. Normal\n 2. Cold Foil\n 3. Holofoil")
            foil = input("Foil: ")


            repeat = input("Input another card (y or n): ")
            if (repeat != "y"):
                break
    elif choice == "2":
        print("asdf")
    elif choice == "3":
        print("affsdf")
    elif choice == "4":
        break
    else:
        break

print("Saving changes.")
