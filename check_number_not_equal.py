# Get input from the user
num1 = float(input("First Number: "))  # Store first number
num2 = float(input("Second Number: "))  # Store second number

# Compare the numbers and determine the smallest
if num1 > num2:
    print("The smallest number is", num2)  # Print num2 if it's smaller
elif num1 < num2:
    print("The smallest number is", num1)  # Print num1 if it's smaller
else:
    print("Both are equal")  # Print equal