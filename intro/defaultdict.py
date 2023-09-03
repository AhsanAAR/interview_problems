from collections import defaultdict

frequencies = defaultdict(int)
string = "Dummy string!"

for character in string:
    frequencies[character] += 1

print("frequencies", frequencies)
