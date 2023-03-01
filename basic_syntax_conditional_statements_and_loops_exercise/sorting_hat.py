command = input()
hat = ""

name_is_valid = True

while command != "Welcome!":
    name = command

    if name == "Voldemort":
        print("You must not speak of that name!")
        name_is_valid = False
        break

    if len(name) < 5:
        hat = "Gryffindor"
    elif len(name) == 5:
        hat = "Slytherin"
    elif len(name) == 6:
        hat = "Ravenclaw"
    else:
        hat = "Hufflepuff"

    print(f"{name} goes to {hat}.")

    command = input()

if name_is_valid:
    print("Welcome to Hogwarts.")
