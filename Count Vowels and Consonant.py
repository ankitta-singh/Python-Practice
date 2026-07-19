

string = input("Enter a string: ").lower()

vowels = 0
consonants = 0

for ch in string:

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of Vowels:", vowels)
print("Number of Consonants:", consonants)