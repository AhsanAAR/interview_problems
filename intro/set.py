occurence = set()

string = "Good a stuff"

for character in string:
    occurence.add(character)

print(occurence, '\n')

if 'a' in occurence:  # O(1)
    print(f'{string} contains "a"')
else:
    print(f'{string} does not contain "a"')
