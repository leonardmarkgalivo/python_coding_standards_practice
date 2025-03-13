# START

# Get the first number from the user
num1 = int(input("Enter first number: "))
result = num1  # Initialize

# Loop to subtract the next 9 numbers
for i in range(9):
    num = int(input("Enter next number: "))
    result -= num

# Display the final result
print("Result:", result)

# END
