# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers and determine the smallest
if num1 > num2:
    print("The smallest number is:", num2)
elif num1 < num2:
    print("The smallest number is:", num1)
else:
    print("Both numbers are equal.")


