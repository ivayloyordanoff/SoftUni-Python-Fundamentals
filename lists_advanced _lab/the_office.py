employees = input().split()
happiness_factor = int(input())

employees = list(map(lambda num: int(num) * happiness_factor, employees))
filtered = list(filter(lambda num: num >= sum(employees) / len(employees), employees))

if len(filtered) >= len(employees) / 2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")
