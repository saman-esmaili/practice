amount = int(input("how many number you want to enter?(choose a number greater than 10)"))
numbers = []
for i in range(amount):
    number = float(input("enter number:"))
    numbers.append(number)

for i in range(9):
    min1 = min(numbers)
    numbers.remove(min1)
final_min = min((numbers))

print(final_min)

