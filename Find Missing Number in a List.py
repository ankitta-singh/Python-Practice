# Problem 6: Find Missing Number in a List

numbers = list(map(int, input("Enter numbers: ").split()))

n = max(numbers)

for i in range(1, n + 1):
    if i not in numbers:
        print("Missing number =", i) 