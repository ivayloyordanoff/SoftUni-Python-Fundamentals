numbers_list = list(map(int, input().split(", ")))
indices = [num for num in range(len(numbers_list)) if numbers_list[num] % 2 == 0]

print(indices)
