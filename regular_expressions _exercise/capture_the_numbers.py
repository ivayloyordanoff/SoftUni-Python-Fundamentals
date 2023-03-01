import re

pattern = r"\d+"

command = input()

while command:
    matches = re.findall(pattern, command)

    if matches:
        print(" ".join(matches), end=" ")

    command = input()
