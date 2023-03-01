command = input()
needed_coffees = 0

while command != "END":
    event = command

    if event == "coding" or event == "dog" or event == "cat" or event == "movie":
        needed_coffees += 1
    elif event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
        needed_coffees += 2

    command = input()

if needed_coffees > 5:
    print("You need extra sleep")
else:
    print(needed_coffees)
