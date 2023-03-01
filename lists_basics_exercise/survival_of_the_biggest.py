import sys

numbers = input().split()
count_of_numbers_to_remove = int(input())

for removal in range(count_of_numbers_to_remove):
    smallest_number = sys.maxsize

    for number in numbers:
        if int(number) < smallest_number:
            smallest_number = int(number)

    numbers.remove(str(smallest_number))

result = ", ".join(numbers)

print(result)
