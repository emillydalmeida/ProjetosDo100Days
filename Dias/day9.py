programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
    student_grades = student_scores
    if student_scores[key] <= 70:
        student_grades[key] = "Fail"
    elif student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    else:
        student_grades[key] = "Outstanding"


print(student_grades)