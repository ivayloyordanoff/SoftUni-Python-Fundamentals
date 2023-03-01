companies = {}

while True:
    command = input()

    if command == "End":
        break

    company_name, employee_id = command.split(" -> ")

    if company_name not in companies:
        companies[company_name] = [employee_id]
    elif company_name in companies and employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

for company_name, employee_id in companies.items():
    print(company_name)
    print("--", "\n-- ".join(employee_id))
