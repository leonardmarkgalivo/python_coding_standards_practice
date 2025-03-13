# Ask the user to enter the first number
num1 = float(input("First Number: "))

#Ask the user to enter the second number
num2 = float(input("Second NUmber "))
#Compare the two numbers:
   # If num1 is greater than num2, print bigger
   # If num1 is less than num2, print bigger yung second
   # If both numbers are equal, print "Both are Equal."
if num1 > num2:
    print("The bigger number is: ", num1)
elif num1 < num2:
    print("The bigger number is: ", num2)
else:
    print("Both are Equal")

