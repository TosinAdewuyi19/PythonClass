total = 0
smallest = float('infinity')
largest = float('-infinity')

for number in range(4):
    number = int(input("Enter an integer"))
    total+=number

if number < smallest:
    smallest = number
if number > smallest:
    largest = number
average = total/4
print('sum', total)
print('Average', average)
print('Smallest', smallest)
print('Largest', largest)

