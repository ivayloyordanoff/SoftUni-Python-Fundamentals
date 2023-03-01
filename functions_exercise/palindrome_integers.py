def is_palindrome(number):
    return number == number[::-1]


numbers = input().split(", ")

for num in numbers:
    print(is_palindrome(num))
