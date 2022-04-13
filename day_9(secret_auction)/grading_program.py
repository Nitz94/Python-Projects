# convert student scores into a student grade dictionary with respect to corresponding grades to the scores

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆



student_grades = {}

#********************OLD CODE***************************

# for key in student_scores:
#     if student_scores[key] > 90:
#         student_scores[key] = "outstanding"
#     elif student_scores[key] <=90 and student_scores[key]<=81:
#         student_scores[key]= " Exeeds Expectations"
#     elif student_scores[key] <= 80 and student_scores[key]>=71:
#         student_scores[key] = " Acceptable"
#     elif student_scores[key]<=70:
#         student_scores[key]="Fail"
#     student_grades=student_scores


#********************************NEW CODE*************************

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = " Exeeds Expectations"
    elif score >70:
        student_grades[student] = " Acceptable"
    else:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)