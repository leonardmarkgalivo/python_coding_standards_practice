even_count = 0

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_count += 1

print(f"Total even numbers: {even_count}")