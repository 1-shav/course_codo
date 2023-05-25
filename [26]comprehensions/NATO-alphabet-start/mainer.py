import pandas

data = pandas.read_csv("code_py/[26]comprehensions/NATO-alphabet-start/phonetic_alphabet.csv")
data_dicti = {row.letter:row.code for (index, row) in data.iterrows()}

while True:
    try:
        stringii = input("Please input the string you want code for: ")
        resultant = [data_dicti[letter] for letter in stringii.upper()]
    except KeyError:
        print("Please input only english letters!")
        continue
    else:
        print(resultant)
        break