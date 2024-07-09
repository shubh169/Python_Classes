num=int(input("Enter your number:"))
sum=0
# for i in range(0,num+1):
#     if i%2==0:
#         sum+=i
# print(f"sum of all even number is {sum}")

for i in range(2,num+1,2):
    sum+=i
print(f"sum of all even number is {sum}")