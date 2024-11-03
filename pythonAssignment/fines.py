days = int(input("Enter number of days: "))

fine = 0
if days <= 5:
    fine = days *  0.50
elif days <= 10:
    fine = (5 * 0.5) + ((days - 5) * 1)
elif days <= 30:
    fine = (5 * 0.5) + (5 * 1) + ((days - 10) * 5)
else :
    print(f"Your membership has been cancelled!")
if days <= 30:
    print(f"The total fine is: Rs {fine}")
    