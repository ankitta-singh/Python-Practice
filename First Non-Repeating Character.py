

string = input("Enter a string: ")

frequency = {}


for ch in string:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1


found = False

for ch in string:
    if frequency[ch] == 1:
        print("First Non-Repeating Character:", ch)
        found = True
        break

if not found:
    print("No Non-Repeating Character Found")


