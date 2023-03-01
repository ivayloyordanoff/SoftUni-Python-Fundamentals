number_of_electrons = int(input())

shells = []

for i in range(1, number_of_electrons + 1):
    max_n = 2 * i ** 2

    if number_of_electrons - max_n <= 0:
        shells.append(number_of_electrons)
        break
    else:
        number_of_electrons -= max_n
        shells.append(max_n)

print(shells)
