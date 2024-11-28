def factorialOf(n):
    if n < 0:
        return None  
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
