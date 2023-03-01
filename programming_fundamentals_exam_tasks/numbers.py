numbers = list(map(int, input().split()))

average_number = sum(numbers) / len(numbers)
greater_than_average = [num for num in numbers if num > average_number]

result = sorted(greater_than_average, reverse=True)

if len(result) > 0:
    print(*result[:5])
else:
    print("No")
