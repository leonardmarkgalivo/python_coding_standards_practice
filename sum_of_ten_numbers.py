#START
#Initialize total to 0.
total = 0
#Repeat 10 times:
   #Ask the user to enter a number.
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))

   #Add the number to total.
    total += num
#Print the total sum.
print("The sum of total numbers is: ", total)
#END
