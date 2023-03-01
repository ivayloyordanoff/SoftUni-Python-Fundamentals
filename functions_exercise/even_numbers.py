def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


numbers = input().split(" ")

list_of_numbers = []

for num in numbers:
    list_of_numbers.append(int(num))

filtered_numbers = list(filter(check_even, list_of_numbers))

print(filtered_numbers)
