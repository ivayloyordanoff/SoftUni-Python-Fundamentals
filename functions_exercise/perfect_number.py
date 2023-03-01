def is_perfect(current_number):
    sum_of_proper_divisors = 0

    for divisor in range(1, current_number):
        if current_number % divisor == 0:
            sum_of_proper_divisors += divisor

    if sum_of_proper_divisors == current_number:
        return "We have a perfect number!"

    return "It's not so perfect."


number = int(input())

print(is_perfect(number))
