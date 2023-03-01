names_list = input().split(", ")
result = sorted(names_list, key=lambda item: (-len(item), item))

print(result)
