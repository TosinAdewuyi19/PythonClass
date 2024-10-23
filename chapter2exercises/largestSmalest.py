largest = float('-inf')
smallest = float('inf')

while True:
    number = int(input("Enter a number: "))

    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

    	choice = input("Do you want to continue?(yes/no): ")

    if choice.lower() != 'y':
        
	print("Largest Number:", largest)
	print("Smallest Number:", smallest)