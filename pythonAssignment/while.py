while True:
    
    first_number = int(input("Enter first number: "))

    
    second_number = int(input("Enter second number: "))

    
    sum = first_number + second_number

    
    print(f"Sum is {sum}")

    
    response = input("Do you want to perform operation again? (yes/no): ")
    if response.lower() != 'yes':
        break
