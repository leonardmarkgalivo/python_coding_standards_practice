#START
#Initialize odd_count to 0.
odd_count = 0
#Repeat 10 times:
for i in range (10):
        num = float(input(f"Enter number {i+1}: "))

        if num % 2 != 0:
            odd_count += 1
   #Ask the user to enter a num.
   #If odd, plus one sa odd_count
#Print the total
print("The number of odd numbers is:", odd_count)
#END
