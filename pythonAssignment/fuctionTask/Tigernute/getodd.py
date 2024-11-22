def get_odd(numbers):
    numbers = [1,2,3,4,5]
    sum = 0
    for number in numbers:
        if number % 2 != 0:
            sum += number

    return sum
numbers = [1,2,3,4,5]
print (get_odd(numbers))