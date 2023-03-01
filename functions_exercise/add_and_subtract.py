def sum_numbers(number_1, number_2):
    return number_1 + number_2


def subtract(sum_of_numbers, number_3):
    return sum_of_numbers - number_3


def add_and_subtract(number_1, number_2, number_3):
    sum_of_number_1_and_number_2 = sum_numbers(number_1, number_2)
    result = subtract(sum_of_number_1_and_number_2, number_3)

    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
