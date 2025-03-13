# START

# Initialize an empty list to store numbers
numbers = []

while True:
    try:
        # Get input from user
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Stopping program.")
        break

# Find and display the highest number
if numbers:
    highest_number = max(numbers)
    print("The highest number is:", highest_number)
else:
    print("No numbers entered.")

# END
