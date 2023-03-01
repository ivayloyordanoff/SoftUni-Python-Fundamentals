numbers = list(map(int, input().split(", ")))
group_capacity = 10

while True:
    current_group = []

    for people in numbers:
        if people <= group_capacity:
            current_group.append(people)

    print(f"Group of {group_capacity}'s: {current_group}")

    [[numbers.remove(x) for x in numbers if x == y] for y in current_group]

    group_capacity += 10

    if len(numbers) == 0:
        break
