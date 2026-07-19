
numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter value of k: "))

k = k % len(numbers)

rotated = numbers[-k:] + numbers[:-k]

print("Rotated List:", rotated) 
