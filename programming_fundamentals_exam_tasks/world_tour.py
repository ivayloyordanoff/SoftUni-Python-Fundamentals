data = input()

while True:
    command = input().split(":")

    current_command = command[0]

    if current_command == "Travel":
        print(f"Ready for world tour! Planned stops: {data}")
        break

    if current_command == "Add Stop":
        index = int(command[1])
        current_string = command[2]

        if 0 <= index < len(data):
            data = data[:index] + current_string + data[index:]

        print(data)

    elif current_command == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])

        if 0 <= start_index <= end_index < len(data):
            data = data[:start_index] + data[end_index + 1:]

        print(data)

    elif current_command == "Switch":
        old_string = command[1]
        new_string = command[2]

        if old_string in data:
            data = data.replace(old_string, new_string)
        print(data)
