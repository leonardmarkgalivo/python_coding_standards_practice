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

# Find the number with the most duplicates
if numbers:
    most_frequent = max(set(numbers), key=numbers.count)
    print("Number with the most duplicates:", most_frequent)
else:
    print("No numbers entered.")

# END
