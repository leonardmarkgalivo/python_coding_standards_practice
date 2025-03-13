# Start

# Initialize odd_count to 0
odd_count = 0

# Repeat 10 times
for i in range(10):
    # Ask the user to enter a number
    num = int(input(f"Enter number {i+1}: "))

    # If the number is odd, increment odd_count
    if num % 2 != 0:
        odd_count += 1

# Print the total count of odd numbers
print("The number of odd numbers is:", odd_count)

# End

