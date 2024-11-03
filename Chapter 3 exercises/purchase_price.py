purchase_price = int(input("Enter purchase price (in cents, 1-100): "))

change = 100 - purchase_price

quarters = change // 25
change %= 25

dimes = change // 10
change %= 10

nickels = change // 5
change %= 5

pennies = change

print("Your change is:")
if quarters > 0:
    print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
if dimes > 0:
    print(f"{dimes} dime{'s' if dimes > 1 else ''}")
if nickels > 0:
    print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
if pennies > 0:
    print(f"{pennies} penn{'ies' if pennies > 1 else ''}")