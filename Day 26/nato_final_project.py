import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict={row.letter:row.code for(index,row) in data.iterrows()}

word=input("Enter the word you would like to:").upper()
output=[phonetic_dict[letter] for letter in word]
print(output)