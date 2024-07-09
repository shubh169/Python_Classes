n=int(input("Enter number of students in list:"))
student_height=[]
for i in range(n):
    x=int(input("Enter student height:"))
    student_height.append(x)
    
length=len(student_height)
sum_of_height=sum(student_height)
avg=sum_of_height/length
print(avg)