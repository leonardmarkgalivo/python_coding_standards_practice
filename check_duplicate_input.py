# START

# Initialize a set to track unique numbers
entered_numbers = set()

# Keep asking for input until an invalid entry is detected
while True:
    try:
        n = int(input("Enter num: "))

        if n in nums:
            print("Duplicate")
        else:
            print("Unique")
            nums.add(n)

    except ValueError:
        print("Invalid input. Stopping program.")
        break

# END
