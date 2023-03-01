strings = input().split()

for string in strings:
    print(''.join(string * len(string)), end='')
