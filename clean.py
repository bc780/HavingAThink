#One time use file to clean the database into the desired format

import pandas as pd

#Convert the excel sheet into a database
df = pd.read_excel("Lorcana Card Database.xlsx")

#Converting the foils column into copies by text to condense the same card into one row
def normalConversion(x) -> int:
    if x.iloc[0] == "Normal":
        return x.iloc[1]
    else:
        return 0
def cfConversion(x) -> int:
    if x.iloc[0] == "Cold Foil":
        return x.iloc[1]
    else:
        return 0
def hfConversion(x) -> int:
    if x.iloc[0] == "Holofoil":
        return x.iloc[1]
    else:
        return 0

df["Normal"] = df[["Foil","Copies"]].apply(normalConversion, axis=1)
df["Cold Foil"] = df[["Foil","Copies"]].apply(cfConversion, axis=1)
df["Holofoil"] = df[["Foil","Copies"]].apply(hfConversion, axis=1)
df = df.drop(columns = "Foil")

df.to_excel("Lorcana Card Database.xlsx")
