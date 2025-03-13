# START

# Initialize lowest number as None
lowest_number = None

while True:
    try:
        # Get input from user
        num = int(input("Enter a number: "))

        # Update the lowest number
        if lowest_number is None or num < lowest_number:
            lowest_number = num

    except ValueError:
        print("Invalid input. Stopping program.")
        break

# Display the lowest number if any valid number was entered
if lowest_number is not None:
    print("The lowest number entered is:", lowest_number)

# END
