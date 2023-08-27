occurence = set()

string = "Good stuff"

for character in string:
    occurence.add(character)

print(occurence, '\n')

if 'a' in occurence:
    print(f'{string} contains "a"')
else:
    print(f'{string} does not contain "a"')
