first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())

all_employees_efficiency_per_hour = first_employee + second_employee + third_employee

hours = 0

while students_count > 0:
    hours += 1

    if hours % 4 == 0:
        continue

    students_count -= all_employees_efficiency_per_hour

print(f"Time needed: {hours}h.")
