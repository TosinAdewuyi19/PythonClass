def rhombus(n):
    number = int(input("Input the number"))
    rhombus(number)


    for a in range(1, n + 1):
        print (" " * (n - 1), end="")

    for b in range (65, 65+a):
        print(chr(a), end="")

    for b in range (65 + a - 2, 64 - 1):
        print (chr(b), end="")

    
