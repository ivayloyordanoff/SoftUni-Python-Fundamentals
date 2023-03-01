year = int(input())

happy_year = False

while not happy_year:
    year += 1
    set_year = set()

    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    if len(set_year) == len(str(year)):
        happy_year = True

print(year)
