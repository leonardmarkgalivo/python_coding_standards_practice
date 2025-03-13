# START

# Get two numbers from the user
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

# Determine the smaller and larger number
start = min(num1, num2)
end = max(num1, num2)

# Loop through numbers between start and end (excluding boundaries)
for num in range(start + 1, end):
    print(num, end=" ")

# END
