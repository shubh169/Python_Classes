print("*********Welcome to the PyPassword Generator**********")
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
         'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','?']
let=int(input("How many letters would you like in your password?:"))
num=int(input("How many numbers you want ?:"))
sym=int(input("How many symbols you want "))
password=[]
for i in range(1,let+1):
    password+=random.choice(letters)
for i in range(1,num+1):
    password+=random.choice(numbers)
for i in range(1,sym+1):
    password+=random.choice(symbols)
random.shuffle(password)

# Converting list to string
new_password=''.join(password)
print(f"Your password is :{new_password}")