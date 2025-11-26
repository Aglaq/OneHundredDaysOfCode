# Day 9 - Dictionaries and Nesting
# Day 9 - Project: Secret Auction

print("Hello, Day 9!")

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    if 90 < student_scores[student]:
        student_grades[student] = "Outstanding"
    elif 80 < student_scores[student]:
        student_grades[student] = "Exceeds Expectations"
    elif 70 < student_scores[student]:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)