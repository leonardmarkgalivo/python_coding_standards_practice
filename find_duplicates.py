# START

# Initialize an empty list to store numbers
numbers = []

# Get 10 numbers from the user
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Find duplicates
duplicates = set([num for num in numbers if numbers.count(num) > 1])

# Display duplicate numbers
print("Numbers with duplicates:", list(duplicates))

# END
