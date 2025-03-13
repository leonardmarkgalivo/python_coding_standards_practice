#START
#Initialize an empty list to store numbers
numbers = []
#Loop indefinitely:
while True:
    try:
        # Get input from user
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Stopping program.")
        break
#Sort the list in descending order
#Display the sorted list
#END