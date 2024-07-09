from art import logo
print(logo)
def caesar(start_text,key,cipher_direction):
    end_text=""
    if cipher_direction=='decode':
        key*=-1
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position+key
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(end_text)    
        
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
          's','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
          's','t','u','v','w','x','y','z']
def start_program():
    direction=input("type encode to encrypt and decode to decrypt\n")
    text=input("Enter your text\n").lower()
    shift=int(input("Type the shift number\n"))
    shift=shift%26
    caesar(start_text=text,key=shift,cipher_direction=direction)
start=True
while True:
    continue_program=input("Do you want to continue program Yes/No:")
    if continue_program=='Yes' or continue_program=='yes':
        start_program()
    else:
        print("Good Bye.")
        break

    
        
