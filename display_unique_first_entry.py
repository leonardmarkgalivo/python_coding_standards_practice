# START
# Initialize an empty list to store user input
numbers = []
seen = set()

# Get 10 numbers from the user
for i in range(10):
    n = int(input("Enter num: "))
    # Add the number to the list only if it's the first occurrence
    if n not in seen:
        nums.append(n)
        seen.add(n)

print("Numbers:", nums)
# Display
# END