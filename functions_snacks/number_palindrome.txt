number = int(input("Enter a five-digit integer: "))

digit1 = number // 10000
digit2 = (number % 10000) // 1000
digit4 = (number % 100) // 10
digit5 = number % 10

if digit1 == digit5 and digit2 == digit4:
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")