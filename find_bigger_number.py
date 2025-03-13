# Ask the user to enter the first number
num1 = float(input("First Number: "))

# Ask the user to enter the second number
num2 = float(input("Second Number: "))

# Compare the two numbers
if num1 > num2:
    print("The bigger number is:", num1)
elif num1 < num2:
    print("The bigger number is:", num2)
else:
    print("Both are equal.")


