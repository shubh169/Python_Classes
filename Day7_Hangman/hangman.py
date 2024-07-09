import random
from hangman_art import stages
from hangman_words import word_list
from hangman_art import logo

print(logo)

chosen_word=random.choice(word_list)
chosen_word_length=len(chosen_word)
display=[]
end_of_games=False
lives=6  
for i in range(chosen_word_length):
    display+="_"

while not end_of_games:
    guess=input("Guess a letter:").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(chosen_word_length):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in display:
        lives-=1
        if lives==0:
            end_of_games=True
            print("You loss!")
#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_games=True
        print("You Win")

    print(stages[lives])
        