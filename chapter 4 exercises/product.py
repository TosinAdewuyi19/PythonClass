def product(*args):
    result = 1 
    for number in args:
       result *= number 
    return result

print(product(10, 25, 3, 4)) 
print(product(10, 20))
print(product(50))
print(product(7, 14, 2)) 
print(product())