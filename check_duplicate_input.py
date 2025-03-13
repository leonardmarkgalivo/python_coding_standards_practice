# START

# Initialize a set
entered_numbers = set()

# Keep asking for input until an invalid entry is detected
while True:
    try:
        # Get user input
        num = int(input("Enter a number: "))

        # Check if the number is already in the set
        if num in entered_numbers:
            print("Duplicate")
        else:
            print("Unique")
            entered_numbers.add(num)

    except ValueError:
        print("Invalid input. Stopping program.")
        break

# END

