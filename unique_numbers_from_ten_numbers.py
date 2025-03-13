# START

# Initialize
numbers = []

# Get 10 numbers from the user
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Find and display unique numbers
unique_numbers = [num for num in numbers if numbers.count(num) == 1]

print("Numbers without duplicates:", unique_numbers)

# END

