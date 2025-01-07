def sum_of_digit(number):
    sum = 0
    while number > 0:
        digit = number % 10 
        sum += digit
        number //= 10
    return sum
if __name__ == "__main__":
    number = int(input("Enter a positive integer: "))
    result = sum_of_digit(number)
    print("The sum of the digits is:", result)