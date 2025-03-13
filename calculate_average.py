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

# Compute and display average if numbers were entered
if numbers:
    average = sum(numbers) / len(numbers)
    print("Average of numbers:", average)
else:
    print("No numbers entered.")

# END

