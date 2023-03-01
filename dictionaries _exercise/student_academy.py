students_and_grades = {}

number_of_grades = int(input())

for current_student in range(number_of_grades):
    student_name = input()
    grade = float(input())

    if student_name not in students_and_grades:
        students_and_grades[student_name] = grade
    else:
        list_grades = [students_and_grades[student_name], grade]
        students_and_grades[student_name] = list_grades

for student, grade in students_and_grades.items():
    if type(grade) == list:
        average_grade = sum(grade) / len(grade)
    else:
        average_grade = grade

    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
