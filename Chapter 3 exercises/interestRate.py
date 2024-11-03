principal = 1000.0  # Initial investment amount
rate = 0.07  # Annual interest rate

for year in range(1, 31):
    amount = principal * (1 + rate) ** year
    print(f"Year {year}: ${amount:.2f}")