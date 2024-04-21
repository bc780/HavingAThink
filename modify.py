import pandas as pd
import tkinter as tk

# Convert the excel sheet into a database
df = pd.read_excel("Lorcana Card Database.xlsx")

#set up main window
def add_item():
    print("test")


def remove_item():
    print("test")


def look_items():
    print("test")

# Create main window
root = tk.Tk()
root.title("Lorcana Card Database Editor")

# Entry for input
labelNum = tk.Label(root, text = "Card Number:")
labelNum.pack(padx=10)
entryNum = tk.Entry(root, width=5)
entryNum.pack(padx=3)

labelExp = tk.Label(root, text = "Expansion Number:")
labelExp.pack(pady=10)
entryExp = tk.Entry(root, width=5)
entryExp.pack(pady=10)

# Listbox to display items
listbox = tk.Listbox(root, width=40)
listbox.pack()

# Buttons
add_button = tk.Button(root, text="Add", command=add_item)
add_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(root, text="Remove", command=remove_item)
remove_button.pack(side=tk.LEFT, padx=5)

look_button = tk.Button(root, text="Look", command=look_items)
look_button.pack(side=tk.LEFT, padx=5)


#start application
root.mainloop()