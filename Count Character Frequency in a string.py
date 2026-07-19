
string = input("Enter a string: ")

frequency = {}

for ch in string:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character Frequencies:")
for key, value in frequency.items():
    print(key, ":", value)
