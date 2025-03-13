#START
#Initialize an empty list to store numbers
numbers = []
# Loop indefinitely:
while True:
    try:
        numbers.append(int(input("Enter num: ")))
    except:
        print("Invalid")
        break
    #If the input is invalid, break the loop
#Identify the highest number entered
#Display the highest number
#END