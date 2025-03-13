# START

# Initialize
numbers = []
seen = set()

# Get 10 numbers from the user
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))

    # Add the number to the list only if its first occurrence
    if num not in seen:
        numbers.append(num)
        seen.add(num)

# Display the numbers
print("Numbers (first entry only for duplicates):", numbers)

# END
