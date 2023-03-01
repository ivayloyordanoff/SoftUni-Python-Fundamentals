number_of_lines = int(input())
word = input()

strings_list = []

for some_strings in range(number_of_lines):
    current_string = input()
    strings_list.append(current_string)

print(strings_list)

for i in range(len(strings_list) - 1, -1, -1):
    element = strings_list[i]

    if word not in element:
        strings_list.remove(element)

print(strings_list)
