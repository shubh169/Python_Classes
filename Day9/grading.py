student_score={
        "shubham":80,
        "bulbul":97,
        "uttam":67,
        "aniket":87,
        "raj":54
                }

student_perfor={}
for name in student_score:
    mark=student_score[name]
    if mark>90:
        student_perfor[name]="outstanding"
    elif mark>80:
        student_perfor[name]="exceeds expectations"
    elif mark>70:
        student_perfor[name]="Acceptable"
    else:
        student_perfor[name]="fail"
        
print(student_perfor)