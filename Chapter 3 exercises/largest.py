largest = float('-inf') 
second_largest = float('-inf')  
for i in range(10):
    number = int(input("Enter a number: "))

    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number

print("Largest:", largest)
print("Second largest:", second_largest)