import random
names=["shubham","karan","raj","amit","toni"]

# dictionary compresion with the help of list.
student_scores={student:random.randint(1,100) for student in names}
print(student_scores)

# dictionary compresion with the help of dictionary.
passed_score={student:score for (student,score) in student_scores.items() if score>50}
print(passed_score)