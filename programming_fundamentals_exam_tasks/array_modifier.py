initial_values = list(map(int, input().split()))

while True:
    command = input()

    if command == "end":
        break

    if command == "decrease":
        for element in range(len(initial_values)):
            initial_values[element] -= 1

        continue

    indexes = command.split()

    first_index = int(indexes[1])
    second_index = int(indexes[2])

    if indexes[0] == "swap":
        initial_values[first_index], initial_values[second_index] = initial_values[second_index], initial_values[
            first_index]

    if indexes[0] == "multiply":
        initial_values[first_index] *= initial_values[second_index]

result = ", ".join([str(element) for element in initial_values])

print(result)
