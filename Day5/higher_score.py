n=int(input("Enter number of students in list:"))
student_score=[]
for i in range(n):
    x=int(input("Enter your score:"))
    student_score.append(x)
    
print("The Highest score in the class is", max(student_score))