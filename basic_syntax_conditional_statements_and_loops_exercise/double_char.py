command = input()

while command != "End":
    if command != "SoftUni":
        for letter in command:
            print(letter * 2, end="")

        print()

    command = input()
