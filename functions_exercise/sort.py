numbers = input().split(" ")

list_of_numbers = []

for number in numbers:
    list_of_numbers.append(int(number))

print(sorted(list_of_numbers))
