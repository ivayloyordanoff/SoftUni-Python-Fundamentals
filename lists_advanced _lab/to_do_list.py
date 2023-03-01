notes = [0] * 10

while True:
    command = input()

    if command == "End":
        break

    split_command = command.split("-")
    priority = int(split_command[0]) - 1
    current_note = split_command[1]
    notes.pop(priority)
    notes.insert(priority, current_note)

result = [element for element in notes if element != 0]

print(result)
