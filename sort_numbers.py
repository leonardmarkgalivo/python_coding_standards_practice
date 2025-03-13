# START

# Initialize an empty list to store numbers
numbers = []

while True:
    try:
        # Get input from user
        num = int(input("Enter a number: "))

        # Add the number to the list
        numbers.append(num)

    except ValueError:
        print("Invalid input. Stopping program.")
        break

# Sort the numbers in ascending order
numbers.sort()

# Display the sorted numbers
print("Numbers in ascending order:", numbers)

# END
