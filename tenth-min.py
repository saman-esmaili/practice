amount = int(input("how many number you want to enter?(choose a number greater than 10)"))
numbers = []
for i in range(amount):
    number = float(input("enter number:"))
    numbers.append(number)
#
# for i in range(9):
#     min1 = min(numbers)
#     numbers.remove(min1)
# final_min = min((numbers))
#
# print(final_min)

# for i in range(len(numbers)):
#     counter = 0
#     for index in range(len(numbers)):
#         if numbers[i] > numbers[index]:
#             counter += 1
#     if counter == 9:
#         print(numbers[i])

index = 0
index2 = 0
counter = 0
for i in range(len(numbers)*len(numbers)):
    if i % len(numbers) == 0 and i != 0:
        if counter == 9:
            print(numbers[index])
        index += 1
        index2 = 0
        counter = 0
    if numbers[index] > numbers[index2]:
        counter += 1
    index2 += 1
