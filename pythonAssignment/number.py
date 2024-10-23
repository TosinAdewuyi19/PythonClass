number = int(input("Please enter an integer between 0 and 1000: "))
if 0 <= number <= 1000:
  
    sum = 0
    while number != 0:
        last_digit = number % 10  
        sum += last_digit     
        number = number // 10
    print(f"The sum of the digits is: {sum}")