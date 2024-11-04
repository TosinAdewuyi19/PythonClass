largest = float('-inf')
second_number = float('-inf')
print("Enter 10 numbers! ")
for number in range(10):
    number = int(input("Enter a number: "))
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_number:
        second_largest = number
print("The largest number is: ", largest)
print("The second-largest is: ", second_largest)

