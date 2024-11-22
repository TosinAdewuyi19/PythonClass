def get_sum(numbers):
    numbers = [2,3,5,6,8,]
    sum = 0
    for number in numbers:
        if number % 2 == 0:
            sum += number

    return sum
numbers = [2,3,5,6,8,]
print (get_sum(numbers))
