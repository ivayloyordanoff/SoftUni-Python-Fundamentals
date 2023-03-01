import re

sentence = input()

pattern = r"\b_([A-Za-z\d]+)\b"
found_names = re.findall(pattern, sentence)

print(",".join(found_names))
