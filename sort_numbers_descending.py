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

# Sort and display numbers in descending order
if numbers:
    numbers.sort(reverse=True)
    print("Numbers from highest to lowest:", numbers)
else:
    print("No numbers entered.")

# END
