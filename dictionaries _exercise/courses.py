courses = {}

while True:
    command = input()

    if command == "end":
        break

    course, name = command.split(" : ")

    if course not in courses:
        courses[course] = [name]
    else:
        courses[course].append(name)

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    print('--', '\n-- '.join(students))
