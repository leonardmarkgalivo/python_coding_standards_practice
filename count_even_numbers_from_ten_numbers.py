# START

# Initialize a counter for even numbers
even_count = 0

# Loop to get 10 numbers from the user
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_count += 1

# Display the total count of even numbers
print(f"Total even numbers: {even_count}")

# END
