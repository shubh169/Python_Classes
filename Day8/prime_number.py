def prime_number(a):
    count=0
    for i in range(1,a+1):
        if number%i==0:
            count+=1
    if count>2:
        print(f"{a} is not a prime number")
    else:
        print(f"{a} is a prime number")
            

number=int(input("Enter your number:"))
if number>2:
    prime_number(number)
else:
    print("Please enter numbers greater than 2. ")