number_of_pieces = int(input())

data = {}

for i in range(number_of_pieces):
    current_data = input().split("|")

    piece = current_data[0]
    composer = current_data[1]
    key = current_data[2]

    data[piece] = [composer, key]

while True:
    command = input()

    if command == "Stop":
        break

    current_command = command.split("|")

    if current_command[0] == "Add":
        piece = current_command[1]
        composer = current_command[2]
        key = current_command[3]

        if piece not in data:
            data[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif current_command[0] == "Remove":
        piece = current_command[1]

        if piece in data:
            data.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif current_command[0] == "ChangeKey":
        piece = current_command[1]
        new_key = current_command[2]

        if piece in data:
            data[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

result = ''

for piece in data:
    composer = data[piece][0]
    key = data[piece][1]

    result += f"{piece} -> Composer: {composer}, Key: {key}\n"

print(result)
