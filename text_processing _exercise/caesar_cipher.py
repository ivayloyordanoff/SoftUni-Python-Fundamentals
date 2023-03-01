start_text = input()

final_text = []

for character in start_text:
    new_character = chr(ord(character) + 3)
    final_text.append(new_character)

print(''.join(final_text))
