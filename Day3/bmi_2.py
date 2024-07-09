weight=float(input("enter your weight in kgs:"))
height=float(input("enter your height in meters:"))
bmi=round(weight/(height**2),2)
if bmi<18.5:
    print("You are underweight.")
elif bmi>18.5 and bmi<25:
    print("You have normal weight.")
elif bmi>25 and bmi<30:
    print("you have slightly overweight.")
elif bmi>30 and bmi<35:
    print("you have obese.")
else:
    print("You have clinically obese.")