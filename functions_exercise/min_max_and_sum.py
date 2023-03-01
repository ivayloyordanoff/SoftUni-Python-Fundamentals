numbers = input().split(" ")

list_of_numbers = []

for number in numbers:
    list_of_numbers.append(int(number))

min_number = min(list_of_numbers)
max_number = max(list_of_numbers)
sum_numbers = sum(list_of_numbers)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_numbers}")
