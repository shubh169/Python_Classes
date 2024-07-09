placeholder="[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names=names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_data:
    letter_content=letter_data.read()
    
for name in names:
    stipped_name=name.strip()
    new_letter=letter_content.replace(placeholder,stipped_name)
    with open(f"./Output/ReadyToSend/letter_for{stipped_name}.txt",mode='w') as final_letter:
        final_letter.write(new_letter)