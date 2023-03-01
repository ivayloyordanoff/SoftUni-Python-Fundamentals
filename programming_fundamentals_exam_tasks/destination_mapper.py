import re

places = input()

pattern = r"(\=|\/)([A-Z][A-Za-z]{2,})\1"
matched = re.finditer(pattern, places)

destinations = []
points = 0

for destination in matched:
    current_destination = re.split("\/|=", destination.group())[1]
    destinations.append(current_destination)
    points += len(current_destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")
