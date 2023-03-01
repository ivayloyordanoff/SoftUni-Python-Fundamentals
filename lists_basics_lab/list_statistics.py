number_of_lines = int(input())

positive = []
negative = []

for numbers in range(number_of_lines):
    current_number = int(input())

    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")
