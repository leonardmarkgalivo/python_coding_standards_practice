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
  # Except:
    #If the input is invalid, break the loop
# If there are numbers in the list:
  #Compute the average
  # Display the average
# Else:
  #Display "No numbers entered."
#END
