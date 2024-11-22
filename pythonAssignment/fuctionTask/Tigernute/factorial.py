def factorial(number):
    result = 1
    n = 0
    for count in (-1, 0 - 1):
        result *= count
    return result