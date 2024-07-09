print("Thank you for choosing Python Pizza Deliveries.")
size=input("Enter the size of pizza S,M,L?:")
add_pepperoni=input("Do you want extra pepperoni? Y,N:?")
extra_cheese=input("Do you want extra cheese in your pizza? Y, N:?")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
else:
    bill+=25
    
if add_pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese=="Y":
    bill+=1
print("Thank you for choosing Python Pizza Deliveries")
print(f"Your final bill is ${bill}.")