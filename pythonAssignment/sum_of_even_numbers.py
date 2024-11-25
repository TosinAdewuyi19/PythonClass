def get_even():
    while True:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        if second_number > first_number:
            break
        else:
            print("The second number must be greater than the first number. Please try again.")
    sum_of_even = sum(counter for counter in range (first_number, second_number + 1)if counter % 2 ==0)

    print(f"The sum of all even numbers between {first_number} and {second_number} is: {sum_of_even}")
if __name__ == "_get_even__":
    get_even()

