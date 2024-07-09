weather=eval(input("enter your weather conditions:"))

output={day:temp*9/5+32 for (day,temp)in weather.items()}

print(output)