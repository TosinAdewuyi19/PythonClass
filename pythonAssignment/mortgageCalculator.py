principal = int(input("Enter the principal amount: "))
rate = int(input("Enter annual interest rate: "))
duration = int(input("Enter duration in years: "))
monthly_rate = (rate/100)/12
duration_in_months = duration*12
payments = principal * ((monthly_rate*(1+monthly_rate)**duration_in_months)/((1+monthly_rate)**duration_in_months-1))

print("Your monthly rate is: %.2f" % payments)