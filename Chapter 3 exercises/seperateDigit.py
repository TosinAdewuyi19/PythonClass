number = int(input("Enter a five-digit integer: "))

temp = number

for i in range(5):
    digit = temp % 10
    print(digit, end=' ')
    temp //= 10